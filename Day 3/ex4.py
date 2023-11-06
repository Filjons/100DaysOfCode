#Pizza program

print("Welcome to pizza program")


size = input("Size? (S, M or L)")
add_pepperoni = input("Do you want pepperoni? (Y or N)")
extra_cheese = input("Extra cheese? (Y or N)")

bill = 0


if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("sizes are S, M or L.")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print("Thank you for choosing Python Pizza!")
print(f"You final bill is: ${bill}")