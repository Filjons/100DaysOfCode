
#silent auction program

bidders = {}

def find_highest_bid():
    highest_bid = 0
    winner = ""

    for bidder in bidders:
        bid = bidders[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    
    print(f"The winner is {winner} with {highest_bid}")

def add_new_bid(new_bidder, new_bid):
    bidders[new_bidder] = new_bid


print("Welcome to the silent auction program!")
name = input("What is your name?\n")
bid = int(input("What is your bid?\n"))

add_new_bid(name, bid)

run = True

while run:
    more_bidders = input("Are there more bidders? (Y/N)\n").upper()
    if more_bidders == "N":
        
        find_highest_bid()
        run = False
        

    else:
        name = input("What is your name?\n")
        bid = int(input("What is your bid?\n"))
        add_new_bid(name, bid)