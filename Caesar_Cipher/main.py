# from utils.Encrypt import encrypt
# from utils.Decrypt import decrypt
from utils.Caesar import caesar
from utils.alphabet import logo

print(logo)
answer = "yes"
while answer == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Not a valid input.")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % 26
        caesar(input_text=text, shift_amount=shift, direction=direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
print("Goodbye!") 
    

# if direction == "encode":
#     print(f"The encoded text is {encrypt(plain_text=text, shift_amount=shift)}")
# elif direction == "decode":
#     print(f"The decoded text is {decrypt(encode_text=text, shift_amount=shift)}")