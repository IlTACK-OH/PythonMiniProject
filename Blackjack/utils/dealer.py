from utils.score import score
from utils.deck import card_deck
import random
def dealer(dealer_cards:list):
    dealer_score = score(dealer_cards)
    while dealer_score < 17:
        dealer_cards.append(random.choice(card_deck))
        dealer_score = score(dealer_cards)
        print(f"Dealer's Cards: {dealer_cards}")
    return dealer_cards