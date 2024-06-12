import random
import os
from utils.art import logo
from utils.deck import card_deck
from utils.user import User
from utils.check_bust import check_bust
from utils.dealer import dealer
from utils.game_process import game_process
from utils.score import score

user = User()
continue_game = True
can_double = True

while continue_game:
    print(logo)
    dealer_cards = random.sample(card_deck, 2)
    user.cards += random.sample(card_deck, 2)
    print(f"You have ${user.money}")
    bet_amount = user.betting(int(input("Please input your betting: $")))
    while True:
        if bet_amount:
            break
        else:
            bet_amount = user.betting(int(input(f"You have {user.money}. please re-enter your betting: $")))

    print(f"Your cards: {user.cards}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    
    check_blackjack = (score(user.cards) == 21)
    if check_blackjack:
        print(f"Dealer's Cards: {dealer_cards}")
        if score(dealer_cards) != 21:
            result = "BlackJack!"
            break
        else:
            result = "Push"
            break
    else:
        while True:
            if can_double == False or (bet_amount > user.money):
                user_choice = input("Type 'hit' or 'stand': ")
                can_double = False # double이 불가능한 상황에서 double을 시도하려는 것을 막기 위함.
            else:
                user_choice = input("Type 'hit' or 'stand' or 'double': ")
            
            if user_choice == 'hit':
                user.hit()
                can_double = False
                if check_bust(user.cards):
                    dealer_cards = dealer(dealer_cards)
                    result = game_process(user.cards, dealer_cards)
                    break
                else:
                    continue
            
            elif user_choice == 'double': # double을 선언하면 카드 1장만 더 받고 자동 stand
                if can_double:
                    bet_amount = user.double(bet_amount)
                    dealer_cards = dealer(dealer_cards)
                    result = game_process(user.cards, dealer_cards)
                    break
                else:
                    continue
            
            elif user_choice == 'stand':
                print(f"Dealer's Cards: {dealer_cards}")
                dealer_cards = dealer(dealer_cards)
                result = game_process(user.cards, dealer_cards)
                break
            
            else:
                continue
            
        print(f"{result}")
        if result == "Win" or result == "BlackJack!":
            user.money += 2*bet_amount
        elif result == "Push":
            user.money += bet_amount
        
        if user.money:
            answer = input("Enter 'y' if you want to proceed to the next round.\nEnter any key if you want to exit the game: ")
            if answer == 'y':
                user.new_round()
                os.system('clear')
            else:
                continue_game = False
        
        else:
            print("You're broke!\nGameOver.")
            continue_game=False