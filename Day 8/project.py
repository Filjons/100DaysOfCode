
import art

def encrypt(plain_text, shift):
    encrypted_message = ""
    for letter in plain_text:

        index = alphabet.index(letter)

        if (index + shift) > len(alphabet):
            index = (index + shift) - len(alphabet)
        else:
            index = index + shift

        encrypted_message += alphabet[index]
    
    print(f"The encoded text is {encrypted_message}")

def decrypt(encrypted_text, shift):
    decrypted_message = ""
    for letter in encrypted_text:

        index = alphabet.index(letter) - shift
        decrypted_message += alphabet[index]
    
    print(f"The encoded text is {decrypted_message}")

def ceasar(text, shift, action):
    message = ""
    if action == "encode":
        for letter in text:

            index = alphabet.index(letter)

            if (index + shift) > len(alphabet):
                index = (index + shift) - len(alphabet)
            else:
                index = index + shift
            message += alphabet[index]
    else:
        for letter in text:

            index = alphabet.index(letter) - shift

            message += alphabet[index]
    print(f"The encoded text is {message}")
             

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphabet = alphabet.split()

art

run = "yes"
while run == "yes":
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #if direction == "encode":
    #    encrypt(plain_text=text, shift=shift)
    #elif direction == "decode":
    #    decrypt(encrypted_text=text, shift=shift)
    #else:
    #    print("Please try again!")
    ceasar(text=text,shift=shift,action=direction)
    run = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
