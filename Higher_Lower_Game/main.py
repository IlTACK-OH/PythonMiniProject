# Higher Lower Game
# 게임에 사용되는 데이터를 기반으로 누가 더 많은 Follower를 가졌는지 맞추는 게임
import os
import time
import utils.art as art
import data.game_data as game_data
import utils.CheckValid as Check
import utils.DataFunc as DataFunc

from utils.game_result import make_result

score = 0
data_set = game_data.data
num_of_data = len(data_set)
used_data = [] # 사용된 데이터 모음

a = DataFunc.get_data(data_set)
used_data.append(a)

# 똑같은 것을 또 뽑았는지 확인하기 위한 코드
check_repeat = False # 초기화
while not check_repeat:
    b = DataFunc.get_data(data_set)
    check_repeat = Check.check_data(used_data, b)
used_data.append(b)

a_info, a_followers = DataFunc.reshape_data(a)
b_info, b_followers = DataFunc.reshape_data(b)
print(f"{art.logo}\nCompare A: {a_info}.\n{art.vs}\nAgainst B: {b_info}.")

check_answer = False # 초기화
# 입력 유효 검사
while not check_answer:
    answer = input("Who has more followers? Type 'A' or 'B': ")
    check_answer = Check.check_answer(answer)

result = make_result(a_followers, b_followers, answer)

while result and len(used_data) < num_of_data:
    os.system('clear')

    a_info, a_followers = b_info, b_followers # 라운드 종료 시 B는 다음 라운드의 a가 된다.
    score += 1
    
    check_repeat = False
    while not check_repeat:
        b = DataFunc.get_data(data_set)
        check_repeat = Check.check_data(used_data, b)    
    used_data.append(b)
    b_info, b_followers = DataFunc.reshape_data(b)
    print(f"{art.logo}\nYou're right! Current score: {score}.")
    print(f"Compare A: {a_info}.\n{art.vs}\nAgainst B: {b_info}.")
    
    check_answer = False # 초기화
    # 입력 유효 검사
    while not check_answer:
        answer = input("Who has more followers? Type 'A' or 'B': ")
        check_answer = Check.check_answer(answer)
    
    result = make_result(a_followers, b_followers, answer)

os.system('clear')
print(art.logo)
if not result:
    print(f"Sorry, that's wrong. final score: {score}")
else:
    print("Crazy! You got all the questions right. Congratulations!")
time.sleep(2)