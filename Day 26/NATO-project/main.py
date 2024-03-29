
'''
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
'''
'''
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
'''

import pandas

words_df = pandas.read_csv("Day 26\\NATO-project\\nato_phonetic_alphabet.csv")

words_dict ={value.letter:value.code for (key, value) in words_df.iterrows()}



while True:
    try:
        word = input("Enter word: ").upper()
        code_list = [words_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        pass
    except KeyboardInterrupt:
        break
    else:
        print(code_list)

