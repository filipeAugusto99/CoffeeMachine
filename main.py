import products
import resources

# TODO 1. Prompt user by asking "What do you like?" (espresso/latte/cappucino)
def available_options():
    input_options = input("What would you like? (espresso/latte/cappuccino): \n").lower()
    return input_options


def show_resources(total):
    for item, qty in resources.items.items():
        unit = "ml" if item != "coffee" else "g"
        print(f"{item.capitalize()}: {qty}{unit}")

    print(f"Money: ${total}")


def check_resources(user_option, menu, coffees_resources, off_coffee_machine):
    ingredients = menu[user_option]["ingredients"]

    for item, required in ingredients.items():
        available = coffees_resources.get(item, 0)

        if available < required:
            print(f"Sorry there is not enough {item}.")
            off_coffee_machine = True
            return False, off_coffee_machine

    return True, off_coffee_machine


def process_coin(coins_resources):
    print("Insert Your Coins\n")
    # qtd_quarters = input(int("Quarters: \n"))
    # qtd_dimes = input(int("Dimes: \n"))
    # qtd_nickles = input(int("Nickles: \n"))
    # qtd_pennies = input(int("Pennies: \n"))

    total = 0

    for type_coin in coins_resources:
        input_qtd_coin = int(input(f"{type_coin.capitalize()}: "))
        total += input_qtd_coin * coins_resources[type_coin]

    return total


def check_transition(drink_name, coins_inserted, menu):
    cost_of_product = menu[drink_name]["cost"]

    if coins_inserted < cost_of_product:
        return "Sorry that's not enough money. Money refunded", False

    change = coins_inserted - cost_of_product

    if change > 0:
        return f"Here is {round(change)} dollars in change.", True

    return "Payment successful.", True


def make_coffee(menu, drink_name, items_machine):
    # water = 0
    # coffee = 0
    # milk = 0
    #
    # for value_ingredient in menu[drink_name]["ingredients"]:
    #     if value_ingredient == "water":
    #         water += menu[drink_name]["ingredients"][value_ingredient]
    #     elif value_ingredient == "coffee":
    #         coffee += menu[drink_name]["ingredients"][value_ingredient]
    #     elif value_ingredient == "milk":
    #         milk += menu[drink_name]["ingredients"][value_ingredient]
    #
    # for item in items_machine:
    #     if item == "water":
    #         items_machine[item] -= water
    #     elif item == "coffee":
    #         items_machine[item] -= coffee
    #     elif item == "milk":
    #         items_machine[item] -= milk
    ingredients = menu[drink_name]["ingredients"]

    for item, amount in ingredients.items():
        items_machine[item] -= amount

    print(f"Here is your {drink_name}☕. Enjoy!")

# TODO 2. Turn off the Coffee Machine
turn_off = False
money_in_machine = 0

while not turn_off:
    option = available_options()

    if option == "off":
        break

# TODO 3. Print Report
    if option == "report":
        show_resources(money_in_machine)
        continue

# TODO 4. Check resources sufficient
#     # method 1
#     for product in products.MENU:
#         if option == product:
#             if resources.items["water"] < products.MENU[product]["ingredients"]["water"]:
#                 print("Sorry there is not enough water")
#             else:
#                 pass
#             if resources.items["coffee"] < products.MENU[product]["ingredients"]["coffee"]:
#                 print("Sorry there is not enough coffee")
#             else:
#                 pass
#             if resources.items["milk"] < products.MENU[product]["ingredients"]["milk"]:
#                 print("Sorry there is not enough milk")
#             else:
#                 pass
    # method two
    enough, turn_off = check_resources(option, products.MENU, resources.items, turn_off)

    if  not enough:
        continue

# TODO 5. Process coins
    coins_inserted = process_coin(resources.coins_types)

# TODO 6. Check Transition successful
    message, ok = check_transition(drink_name=option, coins_inserted=coins_inserted, menu=products.MENU)

    print(message)

    if not ok:
        continue

    money_in_machine += products.MENU[option]["cost"]

# TODO 7. Make a coffee
    make_coffee(products.MENU, option, resources.items)




