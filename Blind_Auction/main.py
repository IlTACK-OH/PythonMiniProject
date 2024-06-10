from utils.auction import auction_process
from utils.admin_mode import password_change, admin_set, load_settings
from utils.logo import logo
import os
import time
import utils.admin_mode as admin_mode

while True:    
    print(logo)
    print("Welcome to the secret auction program!")
    print("If you want to acesss 'Admin Mode', please enter 'admin'.")
    print("If you want to start the a=auction, please enter 'start'.")
    print("If you want to exit, please enter 'exit'")
    mode = input("Enter admin or start or exit: ")

    if mode == 'admin':
        while True: 
            os.system('clear')
            input_password = input("Please enter password: ")   
            if input_password == admin_mode.password:
                os.system('clear')
                p_set_any = input(f"If you want change password enter 'p'. If you want change setting enter 'set'\nIf you want to exit admin mode, enter anything :")
                
                if p_set_any == 'p':
                    password_change()
                    load_settings()
                elif p_set_any == 'set':
                    admin_set()
                    load_settings()
                
                print("Change success")
                time.sleep(3)
                break
            else:
                print("The password is incorrect")
    
    elif mode == 'start':
        auction_process(admin_mode.people_number, admin_mode.min_price)
        do_or_exit = input("please enter 'main' or 'exit': ")
        if do_or_exit == 'exit':
            break
        elif do_or_exit == 'main':
            pass
        else:
            print("Not valid input. Go to the main")
            os.system('clear')
            
    elif mode == 'exit':
        break
        