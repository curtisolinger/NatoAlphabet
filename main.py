import pandas

# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_list = [new_item for item in list]

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_alphabet_data_frame)

# Method 1
# nato_alphabet_dict = {}
# for (index, row) in nato_alphabet_data_frame.iterrows():
#     nato_alphabet_dict[row.letter] = row.code

# Method 2
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data_frame.iterrows()}
# print(nato_alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Declare a list whose elements are the phonetic representations
#   of each letter in a word

# Ask user for a word to convert to phonetic representation
word = input("Enter a word: ").upper()
# Loop through the letters in the user entered word and
#   append the phonetic representation to phonetic_list
phonetic_list = [nato_alphabet_dict[letter] for letter in word]

print(phonetic_list)
