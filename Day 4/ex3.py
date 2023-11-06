line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map = [line1,line2,line3]

print(f"{line1}\n{line2}\n{line3}")
print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to hide the treasure? ")

#Should use abc.index() to get number from letter.  
x = int(position[0])
y = int(position[1])

map[x][y] = "X"

print(f"{line1}\n{line2}\n{line3}")