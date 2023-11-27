'''To do:
1. Print report
2. Check resources sufficient?
3. Process coins
4. Check transaction successful
5. Make coffe'''

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()

def print_menu():
   
    for i in range(0, len(my_menu.menu)):
        name = my_menu.menu[i].name
        cost = my_menu.menu[i].cost
        print(name.upper() + " $" + str(cost) )

def get_cost(drink):
    for i in range(0, len(my_menu.menu)):
        if my_menu.menu[i].name == drink:
            return my_menu.menu[i].cost
        else:
            return -1

while True:
    print("Welcome! Please select a drink:")

    print_menu()
    order = input("Drink: ").lower()
    drink = my_menu.find_drink(order)
    if drink != None:
        if my_coffee_maker.is_resource_sufficient(drink=drink):
            cost = get_cost(drink=drink)
            my_money_machine.make_payment(cost=cost)
            my_coffee_maker.make_coffee(order=drink)
