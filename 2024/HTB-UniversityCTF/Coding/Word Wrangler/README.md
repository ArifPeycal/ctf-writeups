# Word Wrangler
## Description
> The Frontier Archives have sent an encrypted ancient text. As Space Cowboy, your task is to decode it by identifying the most frequently used word. This crucial word could unlock secrets vital to the resistance.

 ## Overview
 Answer Format:
Return the most common word as a single string. Do not include its count in the output.

 Example
Input
Input:
"The quick brown fox jumps over the lazy dog. The dog barks at the fox!"

Output
Output:
the
## Solution
```
import re
from collections import Counter

# Input the text as a single string
input_text = input()  # Example: "The quick brown fox jumps over the lazy dog."

# Normalize the text: Convert to lowercase and remove punctuation
words = re.findall(r'\b\w+\b', input_text.lower())

# Count the occurrences of each word
word_counts = Counter(words)

# Find the most common word
most_common = word_counts.most_common(1)  # Get the most common word and its count

# Output the most common word
print(most_common[0][0])  # Return only the word
```
## Flag
```
HTB{pfupp_wh0_m4d3_th353_345y_ch4ll3ng35_ch1ld1sh!_39615e6964185ce868cce1ec5ce64a45}
```
