from menu import resources, MENU


def print_report(resources, money):
    """Prints a report of all machine resources"""
    output = f"Water: {resources['water']}\n"
    output += f"Milk: {resources['milk']}\n"
    output += f"Coffee: {resources['coffee']}\n"
    output += f"Money: {money:.2f}"
    print(output)


def check_resources(drink, resources):
    """Checks if sufficient ingredients"""
    for ingredient, needed_amount in MENU[drink]['ingredients'].items():
        if needed_amount > resources[ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


profit = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print_report(resources, profit)
        continue
    elif choice == "off":
        is_on = False
    else:
        try:
            drink = MENU[choice]
            if check_resources(choice, resources):
                print(f"{choice} costs {drink['cost']} dollars.")
                payment = process_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(choice, drink['ingredients'])
        except KeyError:
            print("Please select a valid drink")