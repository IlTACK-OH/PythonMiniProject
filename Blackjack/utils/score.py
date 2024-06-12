def score(cards:list):
    cards_sum = 0
    a_list = []
    for card in cards:
        if card in ["J", "Q", "K"]:
            card = 10
        elif card == "A":
            a_list.append(True)
            continue
        cards_sum += card
    
    for _ in a_list:
        if cards_sum + 11 > 21:
            cards_sum += 1
        else:
            cards_sum += 11        
    return cards_sum