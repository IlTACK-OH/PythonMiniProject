def win_algo(my_choose, com_choose) -> str:
    if my_choose == com_choose:
        return "Draw!"
    
    if (my_choose == 0 and com_choose==2) or (my_choose == 1 and com_choose == 0) or (my_choose == 2 and com_choose == 1):
        return "You win"
    else:
        return "You lose"