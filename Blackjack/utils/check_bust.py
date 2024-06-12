from utils.score import score
"""
해당 카드더미가 Bust인지 확인한다.
"""
def check_bust(cards:list):
    cards_sum = score(cards)
    if cards_sum > 21:
        return True
    return False