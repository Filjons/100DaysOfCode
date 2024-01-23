# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# readline() = get list with each line as object
# replace() = replaces a word in a string
# strip() = removes whitespaces from string or word

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# File links
NAME_LIST = "Day 24/Mail Merge Project Start/Input/Names/invited_names.txt"
LETTER_TEMPLATE = "Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt"
OUTPUT_FOLDER = "Day 24/Mail Merge Project Start/Output/ReadyToSend"

# Get a list of names from a file
with open(NAME_LIST) as file:
    list = file.readlines()

names = []
# Remove unvanted chars from names.
for name in list:
    names.append(name.strip())

# Write a new letter to each name in list.

with open(LETTER_TEMPLATE) as file:
    letter = file.read()

# Create a new letter.
for name in names:

    with open(f"Day 24\Mail Merge Project Start\Output\ReadyToSend/{name}_letter.txt", mode="w") as file:
        file.write(letter.replace("[name]", name))
