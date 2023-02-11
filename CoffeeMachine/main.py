MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
}

water_available = resources["water"]
milk_available = resources["milk"]
coffee_available = resources["coffee"]


def update_stock(preference):
    global water_available, coffee_available, milk_available
    if preference == "espresso":
        water_available = water_available - MENU[preference]["ingredients"]["water"]
        coffee_available = coffee_available - MENU[preference]["ingredients"]["coffee"]
        milk_available = milk_available
    elif preference == "latte":
        water_available = water_available - MENU[preference]["ingredients"]["water"]
        coffee_available = coffee_available - MENU[preference]["ingredients"]["coffee"]
        milk_available = milk_available - MENU[preference]["ingredients"]["milk"]
    elif preference == "cappuccino":
        water_available = water_available - MENU[preference]["ingredients"]["water"]
        coffee_available = coffee_available - MENU[preference]["ingredients"]["coffee"]
        milk_available = milk_available - MENU[preference]["ingredients"]["milk"]
    return


def check_stock(preference):
    if (water_available - MENU[preference]["ingredients"]["water"]) >= 0 and (
            coffee_available - MENU[preference]["ingredients"]["coffee"]) >= 0 and milk_available - \
            MENU[preference]["ingredients"]["milk"] >= 0:
        return True
    else:
        if (water_available - MENU[preference]["ingredients"]["water"]) <= 0:
            print(f"The quantity of water is low with {water_available} so cannot make {preference}")
        elif (coffee_available - MENU[preference]["ingredients"]["coffee"]) <= 0:
            print(f"The quantity of coffee is low with {coffee_available} so cannot make {preference}")
        elif (milk_available - MENU[preference]["ingredients"]["milk"]) <= 0:
            print(f"The quantity of milk is low with {milk_available} so cannot make {preference}")
        return False


def update_cost(preference):
    return calculate_cost + MENU[preference]["cost"]


def report():
    print(f"Water: {water_available}")
    print(f"Milk: {milk_available}")
    print(f"Coffee: {coffee_available}")
    print(f"Money: {calculate_cost}")
    return


def transaction(coin_values, preference):
    total = sum(coin_values)
    is_denominations_correct = any(w in coin_values for w in [0.25, 0.10, 0.05, 0.01])
    # print(is_denominations_correct)
    if is_denominations_correct:
        if total < MENU[preference]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif total > MENU[preference]["cost"]:
            balance = round(total - MENU[preference]['cost'], 2)
            print(f"Here is ${balance} in change")
            return True
        elif total == MENU[preference]["cost"]:
            return True
    else:
        print("Pls provide coin denominations of only the following values of $0.25, $0.10, $0.05, $0.01")
        return False


calculate_cost = 0
continue_brewing = True
is_transaction_successful = False
print("Welcome to the Coffee Machine!!")
while continue_brewing:
    drink_preference = input("“What would you like? (espresso/latte/cappuccino): ").lower()
    if drink_preference == 'espresso' or drink_preference == 'latte' or drink_preference == 'cappuccino':
        is_stock_available = check_stock(drink_preference)
        if is_stock_available:
            coins_inserted = [float(x) for x in input(f"Pls insert coins to match ${MENU[drink_preference]['cost']}: ").split()]
            is_transaction_successful = transaction(coins_inserted, drink_preference)
        if is_transaction_successful and is_stock_available:
            print(f"Report before purchasing {drink_preference}")
            report()
            update_stock(drink_preference)
            calculate_cost = update_cost(drink_preference)
            print(f"Here is your {drink_preference}, Enjoy!!")
            print(f"Report after purchasing {drink_preference}")
            report()
        else:
            continue_brewing = False
    elif drink_preference == 'report':
        report()
    elif drink_preference == 'off':
        exit()
    else:
        print("Enter a correct drink you want")
