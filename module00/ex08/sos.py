import sys

# Création du dictionnaire associant les caractères à leur code Morse
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def encode(message):
    message = message.upper()

    morse_code = []
    for char in message:
        if char == ' ':
            morse_code.append('/')
        elif char in MORSE_DICT:
            morse_code.append(MORSE_DICT[char])
        else:
            print("ERROR")
            sys.exit(1)
    return ' '.join(morse_code)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} '<message>'")
        sys.exit(1)
    else:
        message = sys.argv[1]
        result = encode(message)
        print(f"Message original : {message}")
        print(f"Code Morse       : {result}")

if __name__ == "__main__":
    main()