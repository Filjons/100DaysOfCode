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

def calculator():
    num1 = float(input("First number: "))
    
    print_operations()

    should_continue = True
    while should_continue:
        
        operation_symbol = input("Operation: ")
        num2 = float(input("Next number: "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("'Y' to continue or 'N' to reset.").upper() == "Y":
            num1 = answer
        else:
            should_continue = False
            calculator()

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
calculator()
