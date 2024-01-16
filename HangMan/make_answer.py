def make_answer(chosen_word: str, answer_check: list, guess: str = None):
    if not guess:
        return 
    
    for idx, word in enumerate(chosen_word):
        if word == guess:
            answer_check[idx] = word
    return answer_check
