from utils.alphabet import alphabet

def caesar(input_text, shift_amount, direction):
    new_text = ""
    if direction == "encode":
        for char in input_text:
            if char in alphabet:
                plain_idx = alphabet.index(char)
                move_idx = plain_idx + shift_amount
                new_text += alphabet[move_idx]
            else:
                new_text += char
        print(f"The encoded text is {new_text}")
    
    elif direction == "decode":
        for char in input_text:
            if char in alphabet:
                encode_idx = alphabet.index(char)
                move_idx = encode_idx - shift_amount
                new_text += alphabet[move_idx]
            else:
                new_text += char
        print(f"The decoded text is {new_text}")