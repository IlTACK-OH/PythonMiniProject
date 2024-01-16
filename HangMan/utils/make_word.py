import random
# word_list의 단어를 무작위로 선택하는 함수

# 두 개의 경우 함수가 호출될때마다 참조가 발생하는 것보다 전역으로 사용하는 것이 좋다고 생각하였음.
word_list = ["aardvark", "baboon", "camel"]
len_word = len(word_list)

def make_random_word():
    chosen_word = random.choice(word_list)
    return chosen_word