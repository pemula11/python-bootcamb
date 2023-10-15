from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
Coffee = CoffeeMaker()
Money = MoneyMachine()

print(Menu.get_items())


def processing(choice):
    drink = Menu.find_drink(choice)

    if drink is None:
        print("ada yang salah")
        return

    if not Coffee.is_resource_sufficient(drink):
        print("ada yang kurang")
        return

    is_payment_success = Money.make_payment(drink.cost)
    if is_payment_success:

        Coffee.make_coffee(drink)
        print(f"thanks for buying \n")


def machine():
    on = True
    while on:
        choice = input("Pick you choice: Latte/Espresso/Cappuccino : ").lower()
        if choice == 'report':
            Coffee.report()
            Money.report()
        elif choice == 'off':
            on = False
        else:
            processing(choice)

machine()