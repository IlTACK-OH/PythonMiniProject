from utils.alphabet import alphabet

def encrypt(plain_text, shift_amount):
    encode_text = ""
    for char in plain_text:
        plain_idx = alphabet.index(char)
        move_idx = plain_idx + shift_amount
        encode_text += alphabet[move_idx]

    return encode_text
