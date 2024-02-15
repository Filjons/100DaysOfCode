#The game of high or low.

import art
import game_data
from random import randint

#print(game_data)

GAME_DATA = game_data.data
GAME_DATA_LEN = len(GAME_DATA)
VS = art.vs
LOGO = art.logo

score = 0

def welcome_screen():
    print(LOGO)
    print("Welcome to the game of higher lower!\n")
    print("Choose A or B depending on how many followers on inzta!\n")
 
def get_rand(i=-1):
    number = randint(0, GAME_DATA_LEN -1)
    if number == i:
        number = randint(0, GAME_DATA_LEN -1)
    
    return number

def rand_data():
    a = get_rand()
    b = GAME_DATA[a]
    c = GAME_DATA[get_rand(a)]

    return [b,c]

def new_game(pair):
    
    A = pair[0]
    B = pair[1]
    print(f"A = {A['name']} is a {A['description']} from {A['country']}")
    print(VS + '\n')
    print(f"B = {B['name']} is a {B['description']} from {B['country']}")

def get_answer(input):
    a = input[0]['follower_count']
    b = input[1]['follower_count']
    if a > b:
        return 'A'
    elif a < b:
        return 'B'
    else:
        return 'C'

welcome_screen()
run = True
while run:

    data = rand_data()
    new_game(data)
    print(data[0]['follower_count'])
    print(data[1]['follower_count'])

    player = input("A or B? \n").upper()
    if player == get_answer(data):
        score = score +1
        print(f"Correct! Score: {score}\n")
    else:
        print(f"Too bad, that's the wrong answer. Your score was: {score}")
        run = False