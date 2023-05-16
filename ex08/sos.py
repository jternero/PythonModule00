import sys
import string

MORSE_CODE_DICT = {
    'A':'.-', 
    'B':'-...', 
    'C':'-.-.', 
    'D':'-..', 
    'E':'.', 
    'F':'..-.', 
    'G':'--.', 
    'H':'....', 
    'I':'..', 
    'J':'.---', 
    'K':'-.-',
    'L':'.-..', 
    'M':'--', 
    'N':'-.', 
    'O':'---', 
    'P':'.--.', 
    'Q':'--.-', 
    'R':'.-.', 
    'S':'...', 
    'T':'-',
    'U':'..-', 
    'V':'...-', 
    'W':'.--', 
    'X':'-..-', 
    'Y':'-.--', 
    'Z':'--..', 
    '1':'.----', 
    '2':'..---', 
    '3':'...--', 
    '4':'....-', 
    '5':'.....', 
    '6':'-....', 
    '7':'--...', 
    '8':'---..', 
    '9':'----.', 
    '0':'-----', 
    ' ':'/', 
}

def encrypt(message):
    morse = []
    for letter in message.upper():
        if letter in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[letter])
        else:
            return("ERROR")
        
    return ' '.join(morse)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit
    s = ' '.join(sys.argv[1:])
    morse = encrypt(s)
    print(morse)