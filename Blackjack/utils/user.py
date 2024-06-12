import random
from utils.deck import card_deck

class User:
    def __init__(self):
        self.cards = []
        self.money = 1000
    
    def betting(self, bet_amount):
        if self.money >= bet_amount:
            self.money -= bet_amount
            return bet_amount
        return False
    
    def hit(self):
        self.cards.append(random.choice(card_deck))
        print(f"Your cards: {self.cards}")
    
    def double(self, bet_amount):
        self.cards.append(random.choice(card_deck))
        print(f"Your cards: {self.cards}")
        return 2*bet_amount
    
    def new_round(self):
        self.cards = []
        