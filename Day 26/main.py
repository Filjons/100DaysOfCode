# List comprehention excerises
'''
# Ex 1 - Pow of 2
numbers = [1,1,2,3,5,8,13,21,34,55]

print([pow(n,2) for n in numbers])

# Ex 2 - Filter out odd numbers and print the even numbers

list_of_strings = input().split(',')

list_of_ints = [int(n) for n in list_of_strings]

result = [n for n in list_of_ints if n % 2 == 0]

print(result)
'''
# Ex 3 - Compare lists

with open("Day 26\\file1.txt", mode="r") as file:
    list_1 = file.readlines()

#print(list_1)

with open("Day 26\\file2.txt", mode="r") as file:
    list_2 = file.readlines()

#print(list_2)
    
compared_list = [int(n) for n in list_1 if n in list_2]
#result = [int(n) for n in compared_list if n.isdigit()]
print(compared_list)