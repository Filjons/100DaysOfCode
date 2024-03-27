#fruits = eval(input())
fruits = ["1","2","3"]

def make_pie(index):
    try:
        fruit = fruits[index]
        
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(2)