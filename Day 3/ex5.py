print("The love calculator is calculating you score...")

name_1 = input("What is your name?")
name_2 = input("What is their name?")
match_name = name_1 + name_2

true = 0
love = 0

for char in match_name.upper():
    
    if char == "T":
        true += 1
    elif char == "R":
        true += 1
    elif char == "U":
        true += 1
    elif char == "E":
        true += 1

for char in match_name.upper():
    
    if char == "L":
        love += 1
    elif char == "O":
        love += 1
    elif char == "V":
        love += 1
    elif char == "E":
        love += 1

print(f"Score: {true}{love}")