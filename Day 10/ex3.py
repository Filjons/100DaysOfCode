# calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Utills
def print_operations():
    for symbol in operations:
        print(symbol)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print_operations()
operation_symbol = input("Operation: ")

print(f"{num1} {operation_symbol} {num2} = {operations[operation_symbol](num1, num2)}")