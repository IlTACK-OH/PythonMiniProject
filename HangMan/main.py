from utils.make_word import make_random_word as mrw
from utils.make_answer import make_answer
from utils.hangman_art import stages, logo

lives = 6
end_of_game = False
chosen_word = mrw()
answer_check = ["_"] * len(chosen_word)

print(logo)
print("Enter only one letter!")
print("".join(answer_check))  # 선택된 단어의 길이와 같은 길이의 리스트 생성

while not end_of_game:
    guess = input("Guess a letter: ").lower()  # 사용자 입력
    if guess in answer_check:
        print(f"You've already guessed {guess}")
        print(display)
        print(stages[lives])
        continue
    
    answer_check= make_answer(chosen_word, answer_check, guess=guess)  # 게임 진행 저장 리스트
    display = "".join(answer_check)
    # 추측한 문자가 단어에 없을 경우
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

    print(display)
    print(stages[lives])
    # 목숨이 0이 되면 게임 종료(패배)
    if lives == 0:
        end_of_game = True
        print("You lose...")
    # 단어를 맞추면 게임 종료(승리)
    if display == chosen_word:
        end_of_game = True
        print("You win!!!")