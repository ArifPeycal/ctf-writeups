# Difficult Choice
## Description
> In life, we are often faced with the task of making difficult choices and tough decisions... But for now, I'll spare you the dilemma. All you have to do is conquer this challenge and get the flag! Lets find out your capability.

## Solution
- Create a script to extract the poem's letters as 2D array and use index to extract letters.
```python
poem = """Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference."""

# Convert the poem into a 2D array without spaces and commas
poem_2d_array = [list(line.replace(" ", "").replace(",", "")) for line in poem.splitlines()]

# Index pairs
index_pairs = [
    (1, 8), (5, 11), (11, 14), (3, 17), (21, 9), 
    (19, 13), (9, 21), (20, 7), (8, 14), (13, 26), 
    (16, 4), (22, 25), (2, 13), (17, 7), (4, 4), 
    (10, 28), (23, 16)
]

# Extract letters based on the index pairs
extracted_letters = [
    poem_2d_array[row - 1][col - 1] for row, col in index_pairs
]

# Join the letters into a string
result = ''.join(extracted_letters)

print(f"Extracted Letters: {result}")
# Extracted Letters: sealdidealkylelel
```
- Use Vignere Decode ```H03q_C1ak3z_z17L_l1y35_4xb_W3xe3Vd_sW_K3j``` and ```sealdidealkylelel``` as key.
## Flag
```CyGenixCTF{P03m_C1ph3r_w17H_l1n35_4nd_L3tt3Rs_aS_K3y}```
