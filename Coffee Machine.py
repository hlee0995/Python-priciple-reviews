

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
}


def calculate(): 
    print("please insert coins: ")
    total += float(input("How many quarters? ")) * 0.25
    total += float(input("How many nickels? ")) *0.1
    total += float(input("How many dimes? ")) *0.05
    total += float(input("How many pennies? ")) *0.01
    return total

def resource_calculate():
    resources['water'] = MENU[order_id]['ingredients']['water']
    resources['milk'] = MENU[order_id]['ingredients']['milk']
    resources['coffee'] = MENU[order_id]['ingredients']['coffee']
    return resources

def processing(payment, order_id, balance, change):
    if payment < MENU[order_id]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        balance += MENU[order_id]['cost']
        change = payment - MENU[order_id]['cost']
        print(f"Here is your {order_id} and change of ${change}")
        resource_calculate()

        return balance, change



status = True
balance = 0
change = 0


while status:
    order_id=(input("What would you like? (espresso/latte/cappuccino): "))
    if order_id == "off" :
        print("Machine will be terminated")
        status = False
    elif order_id == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Balance is ${balance}")
    else: 
        payment = calculate()
        processing(payment, order_id, balance, change)



 






