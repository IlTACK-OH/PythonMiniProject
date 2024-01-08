import random
from graphicRSP import choose_graphic
from win_algo import win_algo

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

my_choose = int(input())
com_choose = random.randint(0,2)
if my_choose >= 3 or my_choose < 0:
    print("You typed an invalid number, please restart game")
else:
    print("\n" + choose_graphic(my_choose) + "\nComputer choose:\n"+choose_graphic(com_choose)+"\n")
    print(win_algo(my_choose, com_choose))
    print("\n-")
