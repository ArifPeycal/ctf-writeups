# Conflict Cruncher


## Overiew
Your mission is to merge these conflicting data streams into a single dictionary. When conflicts arise (identical keys), you must apply the Frontier Protocol: retain the value from the second dictionary and discard the conflicting value from the first.

Complete this task swiftly and accurately, Cowboy, and report the unified dictionary back to Lena Starling. The fate of the resistance may depend on it!

Example
Input
String Dict input: {'a': 1, 'b': 2, 'c': 3}, {'b': 4, 'd': 5}

Output
Merged Output: {'a': 1, 'b': 4, 'c': 3, 'd': 5}

## Solution
```python
# Input two dictionaries as strings
dict1_str = input()
dict2_str = input()

# Convert the input strings to actual dictionaries
dict1 = eval(dict1_str)
dict2 = eval(dict2_str)

# Merge dict1 and dict2, with dict2 taking precedence on conflicts
merged_dict = dict1.copy()  # Start with a copy of dict1
merged_dict.update(dict2)   # Update with dict2 (overwrites conflicting keys)

# Print the merged dictionary
print(merged_dict)
```
## Flag
```
HTB{n0w_1m_0ff1c4lly_4_c0nfl1ct_crunch3r_y4y!_7094f4d571dd7cad616e36e7b7ba8196}
```
