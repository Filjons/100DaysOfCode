import random
def blank_space(length):
    word = []
    for n in range(0, length):
        word.append('_')
    return word

def replace_blank(letter):

    index = 0
    for n in range(0, random_word_len-1):
        i = random_word.find(letter,index)
        if i != -1:
            index = i
            word[index] = letter

    print(word)
  
def game_over(word):
    if "_" in word:
        return 0
    else:
        return 1


word_list = ["cat","dog","hat","dot"]

r = random.randint(0, len(word_list) -1)
random_word = word_list[r]
random_word_len = len(random_word)

word = blank_space(random_word_len)
guesses = 5

print("Welcome to hangman!")
print(f"You have {guesses} tries!")

while guesses > 0:
    letter = input("Guess a letter: ").lower()
    guesses -= 1

    if letter in random_word:
        print("Correct!")
        replace_blank(letter)
        
        if game_over(word):
            print("You win!")
            guesses = 0
    else:
        print("Wrong guess. Please try again.")

print("Thank you for playing!")