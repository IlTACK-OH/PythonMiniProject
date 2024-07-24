def input_and_check(choice_price:int):
    quarters = int(input("How many quarters?: "))*0.25
    dimes = int(input("How many dimes?: "))*0.10
    nickles = int(input("How many nickles?: "))*0.05
    pennies = int(input("How many pennies?: "))*0.01
    total = round(quarters + dimes + nickles + pennies, 2)
    
    if total < choice_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    print(f"Here is ${round(total - choice_price,2)} in change.")
    return True 