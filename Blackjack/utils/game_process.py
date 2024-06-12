from utils.score import score
"""
이 파일에서는 Blackjack 경기에서 누가 이겼는지 판단하는 코드를 담고 있다.
아래 함수의 입력은 다음과 같다.
user: 유저가 받은 카드더미.
dealer: 딜러의 카드더미.
"""

def game_process(user_cards:list, dealer_cards:list):
    user_sum = score(user_cards)
    dealer_sum = score(dealer_cards)
            
    # User Card덱의 합이 21이상일때
    if user_sum > 21:
        if dealer_sum <= 21:
            return "Lose"
        elif dealer_sum > 21:
            return "Push"
    
    # User Card덱의 합이 21일때
    if user_sum == 21:
        if dealer_sum != 21:
            return "Win"
        elif dealer_sum == 21:
            return "Push"
    
    # User Card덱의 합이 21미만일때
    if user_sum < 21:
        if dealer_sum > 21:
            return "Win"
        elif user_sum > dealer_sum:
            return "Win"
        elif user_sum == dealer_sum:
            return "Push"
        else:
            return "Lose"