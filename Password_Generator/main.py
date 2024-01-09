#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
len_letters = len(letters)
len_symbols = len(symbols)

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# 무작위로 고른 숫자를 통해 빈리스트에 추가 후 셔플
choose_password = []
for _ in range(nr_symbols):
    choose_password.append(random.choice(symbols))

for _ in range(nr_numbers):
    choose_password.append(random.choice(numbers))

for _ in range(nr_letters-(nr_numbers+nr_symbols)):
    choose_password.append(random.choice(letters))

random.shuffle(choose_password)
gen_password = "".join(choose_password)
print("Here is your password: " + gen_password)