
# File paths in Windows uses \ (back slash). For the path to work in Python use / (forward slash)
file = open("C:/Users/filjon/OneDrive - Mildef/Dokument/Code/100DaysOfCode/Day 24/my_file.txt")
content = file.read()
file.close()
print(content)

# This method auto-closes the file after use! Saves memory
with open("C:/Users/filjon/OneDrive - Mildef/Dokument/Code/100DaysOfCode/Day 24/my_file.txt", mode="r") as file:
    content = file.read()
    print(content)

# If the file dows not exist then Python will create it. Write mode will delete the previoius text and add the new one. 
with open("C:/Users/filjon/OneDrive - Mildef/Dokument/Code/100DaysOfCode/Day 24/my_file.txt", mode="w") as file:
    file.write("Hello world!")

with open("C:/Users/filjon/OneDrive - Mildef/Dokument/Code/100DaysOfCode/Day 24/my_file.txt", mode="r") as file:
    content = file.read()
    print(content)

# Append mode will add the new text to the old text
with open("C:/Users/filjon/OneDrive - Mildef/Dokument/Code/100DaysOfCode/Day 24/my_file.txt", mode="a") as file:
    file.write("\nAppended text")

with open("C:/Users/filjon/OneDrive - Mildef/Dokument/Code/100DaysOfCode/Day 24/my_file.txt", mode="r") as file:
    content = file.read()
    print(content)

with open("C:/Users/filjon/OneDrive - Mildef/Dokument/Code/100DaysOfCode/Day 24/my_file.txt", mode="w") as file:
    file.write("ello world!")
