sentence = input()

list_of_words = sentence.split()

dict_of_words = {word:len(word) for word in list_of_words}

print(dict_of_words)