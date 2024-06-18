import random
def new_game(mode="easy"):
    thinking_num = random.choice(range(1,101))
    while True:
        if mode == "easy":
            avail_num = 10
            break
        elif mode == "hard":
            avail_num = 5
            break
        else:
            mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
            
    while avail_num > 0 :
        print(f"You have {avail_num} attempts remaining to guess the number.")
        try:
            guess_num = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please re-enter.")
            guess_num = int(input("Make a guess: "))
        
        if guess_num == thinking_num:
            print(f"You got it! The answer was {guess_num}")
            break
        
        else:
            avail_num -= 1
            if guess_num < thinking_num:
                print("\nLow.\n")
            else:
                print("\nHigh.\n")
            print("Guess again.")
            
            
        