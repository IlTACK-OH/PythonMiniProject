import random
from utils.word_list import word_list 

# word_list의 단어를 무작위로 선택하는 함수
def make_random_word():
    chosen_word = random.choice(word_list)
    return chosen_word