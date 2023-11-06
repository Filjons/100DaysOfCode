#Tip calculator

#Ask for total bill cost
bill = input("What was the total bill?\n$")
tip = input("What precentage tip would you like to give?\n:")
peps = input("How many people to split the bill?\n:")

#calculate the total
answer = (float(bill) * (1 + (int(tip)/100))) / int(peps)

#Round the final answer with .format
cost = "{:0.2f}".format(answer)

print(f"Each person should pay: ${cost}")