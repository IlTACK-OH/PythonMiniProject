from utils.alphabet import alphabet

def decrypt(encode_text, shift_amount):
    decode_text =""
    for char in encode_text:
        encode_idx = alphabet.index(char)
        move_idx = encode_idx - shift_amount
        decode_text += alphabet[move_idx]
    
    return decode_text