#project-
#coffee machine


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 76,
    "money": 2.5,
}

# Coffee menu with prices and resource requirements
menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
}

# Function to print the current resource report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

# Function to check if there are enough resources to make the drink
def check_resources(drink):
    for item in menu[drink]:
        if item != "cost" and menu[drink][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Function to process coins and calculate total money inserted
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return round(quarters + dimes + nickels + pennies, 2)

# Function to handle the transaction and provide change if necessary
def handle_transaction(drink, payment):
    if payment >= menu[drink]["cost"]:
        change = round(payment - menu[drink]["cost"], 2)
        print(f"Here is ${change} in change.")
        resources["money"] += menu[drink]["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Function to make the coffee and deduct resources
def make_coffee(drink):
    for item in menu[drink]:
        if item != "cost":
            resources[item] -= menu[drink][item]
    print(f"Here is your {drink}. Enjoy!")

# Main function to run the coffee machine program
def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino)(if not enter'off'): ").lower()
        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif choice == "report":
            print_report()
        elif choice in menu:
            if check_resources(choice):
                payment = process_coins()
                if handle_transaction(choice, payment):
                    make_coffee(choice)
        else:
            print("Invalid input. Please choose from espresso, latte, or cappuccino.")

# Run the coffee machine program
coffee_machine()
