#Number guessing game
from random import randint
def print_attempts():

    if attempts == 0:
        print("You do not have any guesses left!")
        return False
    elif attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
    
    return True

def decrease_attempts():

    return attempts - 1

def check_guess(guess):

    if guess == secret_number:
        print("You win!")
        return False
    elif guess > secret_number:
        print("Too high.")
    elif guess < secret_number:
        print("Too low.")
    
    return True

secret_number = randint(1, 100)
player = 0
attempts = 5

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

run = True

while run:
    if print_attempts():
        player = int(input("Make a guess: "))
        attempts = decrease_attempts()
        run = check_guess(player)
    
