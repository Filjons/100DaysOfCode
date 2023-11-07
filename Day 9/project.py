
#silent auction program

bidders = {}

def find_highest_bid():
    bid_list = bidders.values()
    bidders_list = bidders.keys()
    max =  max(bid_list)
    max_index = bid_list.index(max)
    max_bidder = bidders_list[max_index]
    print(f"The winner is {max_bidder} with {max}")
    

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