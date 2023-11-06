#Rock, paper and scissors game
import random

rps = ["Rock","Paper","Scissors"]

computer = random.randint(0,2)

player = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors:"))

print(f"You chose {rps[player]}!")
print(f"Computer chose {rps[computer]}!")

if player == computer:
    print("It's a draw!")
elif player < computer:
    if computer - player == 1:
        print("Computer wins!")
    else:
        print("You win!")
else:
    print("You win!")