from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turn_off = False

while not turn_off:
    option = input((f"What would you like? ({menu.get_items()})\n")).lower()

    if option == "off":
        break

    if option == "report":
        coffee_maker.report()
        continue


    find_item = menu.find_drink(option)

    enough = coffee_maker.is_resource_sufficient(find_item)
    
    if enough == False:
        break

    cost = find_item.cost
    order = find_item.name

    payment = money_machine.make_payment(cost=cost)

    if payment == True:
        coffee_maker.make_coffee(find_item)

    # payment = money_machine.make_payment(cost=cost)