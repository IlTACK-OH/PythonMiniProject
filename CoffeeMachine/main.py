import os
import time
from utils import menu, report, price, resource

menu_dict = menu.MENU
machine_resources = menu.resources
profit = 0
while True:
    choice = input("What would you like?\nespresso($1.5)   latte($2.5)   cappuccino($3.0): ")
    if choice == 'off':
        break
    
    elif choice in['report', 'Report', 'REPORT']:
        report.make_report(machine_resources, profit)
        time.sleep(5)
    
    elif choice in ['espresso', 'latte', 'cappuccino']:
        choice_ingre = menu_dict[choice]['ingredients']
        # 1. 자원이 충분한지 확인
        if resource.resource_suff(choice_ingre, machine_resources):      
            # 2. 동전을 입력받고 충분한지 처리
            choice_price = menu_dict[choice]['cost']
            if price.input_and_check(choice_price):
                print(f"Here is your {choice.title()} ☕️ Enjoy!")
                profit += choice_price
                resource.modify_resource(machine_resources, choice_ingre)
                
    else:
        print("Invalid input. Please re-enter.")
        
    
    time.sleep(5)
    os.system('clear')