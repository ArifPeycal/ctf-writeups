from itertools import product

# List of potential words
words = ['Portofino', 'Tiramisu', 'Milan', 'Starbucks', 'Berlin', 'Italy', 'Netherlands', 'Swans', 'Swarovski', 'Amsterdam']

# List of possible date formats
date_formats = ['04081965', '19650408', '08041965', '19650804','0481965','481965','1965408','196548','8041965','0841965']

# Function to generate all combinations
def generate_wordlist(words, date_formats):
    wordlist = []
    
    for word_combo, date_format in product(product(words, repeat=3), date_formats):
        # Upper and lower case variations for each word in the combination
        for word in word_combo:
            entry = ''.join(word_combo) + date_format
            wordlist.append(entry)
            wordlist.append(entry.upper())
            wordlist.append(entry.lower())
    
    return wordlist

# Generate wordlist
result_wordlist = generate_wordlist(words, date_formats)

result_wordlist = list(set(result_wordlist))
# Write wordlist to file
with open('wordlist.txt', 'w') as file:
    for item in result_wordlist:
        file.write(item + '\n')

print(f"{len(result_wordlist)} passwords have been created and written to wordlist.txt.")
