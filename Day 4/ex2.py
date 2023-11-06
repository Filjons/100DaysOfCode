import random

names = ["Angela","Ben","Jenny","Michael","Chloe"]

names_len = len(names)
ran_num = random.randint(0, names_len -1)

name = names[ran_num]
print(f"{name} is going to buy the meal today!")
