import os
from utils.logo import logo
def auction_process(people_num, min_price):
    submit_num = 0 # 입찰 가격을 제출한 사람
    auction_dict = {} # 입찰 내역 저장
    # 입찰 과정 반복문
    while submit_num < people_num:
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        
        while price < min_price:
            price = int(input(f"The minimum bid is ${min_price}. Please rewrite bid $"))
        
        submit_num += 1
        auction_dict[name] = price
        os.system('clear') # 출력제거
        print(logo)
    
    winner = max(auction_dict, key=auction_dict.get) # 최종 입찰자
    print(f"The winner is {winner} with a bid of ${auction_dict[winner]}")
    