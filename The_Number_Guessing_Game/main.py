from utils import logo
from utils import game
import os

while True:
    print(logo.logo)
    print("Welcome to the the Number Guessing Game!")
    print("I'm thinking of a Number between 1 and 100.")

    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    new_game = game.new_game(mode)
    con_game = input("Enter 'y' to continue the game.\nEnter any key if you want to exit the game: ")
    if con_game == 'y' or con_game == 'Y':
        os.system('clear')
        continue
    else:
        break
    