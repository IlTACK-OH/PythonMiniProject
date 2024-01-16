from utils.make_word import make_random_word as mrw
from utils.make_answer import make_answer
from utils.hangman_art import stages, logo

lives = 6
end_of_game = False
chosen_word = mrw()
answer_check = ["_"] * len(chosen_word)

print(logo)
print("".join(answer_check))  # 선택된 단어의 길이와 같은 길이의 리스트 생성

while not end_of_game:
    guess = input("Guess a letter: ").lower()  # 사용자 입력
    answer_check= make_answer(chosen_word, answer_check, guess=guess)  # 입력 문자가 단어에 있으면 display변환
    display = "".join(answer_check)
    print(display)
    if guess not in chosen_word:
        lives -= 1
    
    print(stages[lives])
    if lives == 0:
        break
    
    if display == chosen_word:
        end_of_game = True
        print("You win!!!")

if not end_of_game:
    print("You lose...")