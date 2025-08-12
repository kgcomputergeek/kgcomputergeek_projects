"""
iterate pandas dataframe and create a dictionary 

# import pandas as pd

# #read the csv file
# data = pd.read_csv("nato_phonetic_alphabet.csv")

# #create a dictionary of the phonetic code words from a word that the user inputs.
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(phonetic_dict)

#to-do list
#1 create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#2 create a list of the phonetic code words from a word that the user inputs.

#Hints:
#1 You might want to create a dictionary of phonetic code words from the NATO alphabet.
#2 Maybe you could start with a word like "Alfa" and see if you can find it in the NATO dict.

"""

import pandas as pd

# Read the CSV file (not the Python file!)
data = pd.read_csv("day26_files/NATO-alphabet-start/nato_phonetic_alphabet.csv")

# Create a dictionary of the phonetic code words
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs
user_input = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in user_input]
print(output_list)



