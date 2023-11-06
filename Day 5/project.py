import string
import random

#could have used random.choice and random.shuffle or list.shuffle

letters = list(string.ascii_letters)
random_letters = []

numbers = list(string.digits)
random_numbers = []

symbols = list(string.punctuation)
random_symbols = []

password = []

print("Welcome to the password generator!")

nr_letters = int(input("How many letters would you like to use?\n"))

for n in range(0, nr_letters):
    r = random.randint(0,len(letters)-1)
    random_letters.append(letters[r])

nr_symbols = int(input("How many symbols would you like to use?\n"))

for n in range(0, nr_symbols):
    r = random.randint(0,len(symbols)-1)
    random_symbols.append(symbols[r])

nr_numbers = int(input("How many numbers would you like to use?\n"))

for n in range(0, nr_numbers):
    r = random.randint(0,len(numbers)-1)
    random_numbers.append(numbers[r])

password_length = len(random_letters) + len(random_numbers) + len(random_symbols)
print(f"Password length is {password_length}")

data = [random_letters, random_symbols, random_numbers]

while password_length > 0:
    seed = random.randint(0,2)

    if len(data[seed]) != 0:
        password.append(data[seed].pop())
        password_length -= 1

password_str = map(str, password)

password = ''.join(password_str)
print(f"The password is: {password}")


