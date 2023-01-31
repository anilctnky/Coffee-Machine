MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

is_off = False


def adjust_ingredients(selected_drink, drink_name):
    my_ing = selected_drink["ingredients"]
    if drink_name == "latte":
        resources["water"] -= my_ing["water"]
        resources["milk"] -= my_ing["milk"]
        resources["coffee"] -= my_ing["coffee"]
        resources["money"] += 2.5
    elif drink_name == "cappuccino":
        resources["water"] -= my_ing["water"]
        resources["milk"] -= my_ing["milk"]
        resources["coffee"] -= my_ing["coffee"]
        resources["money"] += 3.0
    elif drink_name == "espresso":
        resources["water"] -= my_ing["water"]
        resources["coffee"] -= my_ing["coffee"]
        resources["money"] += 1.5


def get_report():
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: {resources["money"]}')


def is_price_enough(money, cost):
    if money > cost:
        return True
    else:
        return False


def check_sufficient(data1, name):
    ingredients = data1["ingredients"]
    if name == "latte":
        if ingredients["water"] > resources["water"]:
            return "water"
        elif ingredients["milk"] > resources["milk"]:
            return "milk"
        elif ingredients["coffee"] > resources["coffee"]:
            return "coffee"
        else:
            return True
    elif name == "cappuccino":
        if ingredients["water"] > resources["water"]:
            return "water"
        elif ingredients["milk"] > resources["milk"]:
            return "milk"
        elif ingredients["coffee"] > resources["coffee"]:
            return "coffee"
        else:
            return True
    elif name == "espresso":
        if ingredients["water"] > resources["water"]:
            return "water"
        elif ingredients["coffee"] > resources["coffee"]:
            return "coffee"
        else:
            return True

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):


while not is_off:
    drink_choice = input("What would you like? espresso/latte/cappuccino\n")
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if drink_choice == "off":
        is_off = True
    # TODO: 3. Print report.
    elif drink_choice == "report":
        get_report()
    else:
        current_selection = MENU[drink_choice]
        # TODO: 4. Check resources sufficient?
        ingredients_check = check_sufficient(current_selection, drink_choice)
        if check_sufficient(current_selection, drink_choice) == True:
            paid_total = 0
            print("Please insert coins.")
            # TODO: 5. Process coins.
            paid_total += int(input("How many quarters?: ")) * 0.25
            paid_total += int(input("How many dimes?: ")) * 0.10
            paid_total += int(input("How many nickels?: ")) * 0.05
            paid_total += int(input("How many pennies?: ")) * 0.01
            cost_total = current_selection["cost"]
            if is_price_enough(paid_total, cost_total):
                charge = paid_total - cost_total
                print(f"You paid total ${paid_total}. Here is ${charge:.2f} in change.")
                print(f"Here is your {drink_choice}, enjoy!")
                adjust_ingredients(current_selection, drink_choice)
            else:
                print("Sorry your money is not enough. Money refunded.")

        else:
            if ingredients_check == "water":
                print("Sorry, there is not enough water.")
            elif ingredients_check == "coffee":
                print("Sorry, there is not enough coffee.")
            elif ingredients_check == "milk":
                print("Sorry, there is not enough milk")

    # elif drink_choice == "espresso":
    #     current_selection = MENU["espresso"]
    #     # TODO: 4. Check resources sufficient?
    #     ingredient_check = check_sufficient(current_selection, drink_choice)
    #     if check_sufficient(current_selection, drink_choice) == True:
    #         print("Please insert coins.")
    #         quarters_no = int(input("How many quarters?: "))
    #         dimes_no = int(input("How many dimes?: "))
    #         nickels_no = int(input("How many nickels?: "))
    #         pennies_no = int(input("How many pennies?: "))
    #         # TODO: 5. Process coins.
    #         paid_total = quarters_no * 0.25 + dimes_no * 0.10 + nickels_no * 0.05 + pennies_no * 0.01
    #         cost_total = current_selection["cost"]
    #         if is_price_enough(paid_total, cost_total):
    #             charge = paid_total - cost_total
    #             print(f"You paid total ${paid_total}. Here is ${charge:.2f} in change.")
    #             print(f"Here is your {drink_choice}, enjoy!")
    #             adjust_ingredients(current_selection, drink_choice)
    #         else:
    #             print("Sorry your money is not enough.")
    #
    #     else:
    #         if ingredient_check == "water":
    #             print("Sorry, there is not enough water.")
    #         elif ingredient_check == "coffee":
    #             print("Sorry, there is not enough coffee.")
    #         elif ingredient_check == "milk":
    #             print("Sorry, there is not enough milk")
    #
    # elif drink_choice == "cappuccino":
    #     current_selection = MENU["cappuccino"]
    #     # TODO: 4. Check resources sufficient?
    #     ingredient_check = check_sufficient(current_selection, drink_choice)
    #     if check_sufficient(current_selection, drink_choice) == True:
    #         print("Please insert coins.")
    #         quarters_no = int(input("How many quarters?: "))
    #         dimes_no = int(input("How many dimes?: "))
    #         nickels_no = int(input("How many nickels?: "))
    #         pennies_no = int(input("How many pennies?: "))
    #         # TODO: 5. Process coins.
    #         paid_total = quarters_no * 0.25 + dimes_no * 0.10 + nickels_no * 0.05 + pennies_no * 0.01
    #         cost_total = current_selection["cost"]
    #         # TODO: 6. Check transaction successful?
    #         # TODO: 7. Make Coffee.
    #         if is_price_enough(paid_total, cost_total):
    #             charge = paid_total - cost_total
    #             print(f"You paid total ${paid_total}. Here is ${charge:.2f} in change.")
    #             print(f"Here is your {drink_choice}, enjoy!")
    #             adjust_ingredients(current_selection, drink_choice)
    #         else:
    #             print("Sorry your money is not enough.")
    #
    #     else:
    #         if ingredient_check == "water":
    #             print("Sorry, there is not enough water.")
    #         elif ingredient_check == "coffee":
    #             print("Sorry, there is not enough coffee.")
    #         elif ingredient_check == "milk":
    #             print("Sorry, there is not enough milk")


