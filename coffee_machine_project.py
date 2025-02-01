options = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 150
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,  # Espresso doesn't need milk
            "coffee": 24
        },
        "cost": 100
    },
    "cappuccino": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 50
        },
        "cost": 200
    },
}

report = {
    "resources": {
        "water": 1000,
        "milk": 400,
        "coffee": 200
    }
}


def check_resources(selected_coffee, options):
    """Check if there are enough resources to make the selected coffee."""
    for ingredient, amount in options[selected_coffee]["ingredients"].items():
        if report["resources"][ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return taking_money(selected_coffee, options)


def taking_money(selected_coffee, options):
    """Handle the payment process."""
    global profit
    print("Please insert coins:")

    try:
        fives = int(input("How many 5Rs. coins? "))
        tens = int(input("How many 10Rs. coins? "))
        twenties = int(input("How many 20Rs. coins? "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return False

    total = (fives * 5) + (tens * 10) + (twenties * 20)

    if total < options[selected_coffee]["cost"]:
        print(f"Your money Rs.{total} is not enough. Here is your money back!")
        return False
    else:
        if total > options[selected_coffee]["cost"]:
            print(f"Here is your Rs.{total - options[selected_coffee]['cost']} in change.")

        # Deduct ingredients from report
        for ingredient, amount in options[selected_coffee]["ingredients"].items():
            report["resources"][ingredient] -= amount

        profit += options[selected_coffee]["cost"]
        print(f"Here is your {selected_coffee} ☕. Enjoy!")
        return True


profit = 0
repeat = True

while repeat:
    choice = input("\nWhat would you like to have? (latte/espresso/cappuccino/report/off): ").lower()

    if choice == "report":
        print("\n--- Machine Report ---")
        for resource, amount in report["resources"].items():
            print(f"{resource.capitalize()}: {amount}ml")
        print(f"Money: Rs.{profit}")
    elif choice == "off":
        print("Turning off the coffee machine. Goodbye! ☕")
        repeat = False
    elif choice in options:
        check_resources(choice, options)
    else:
        print("Invalid choice. Please select from latte, espresso, or cappuccino.")
