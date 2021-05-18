morse_code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
              'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
              'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
              'y': '-.--', 'z': '--..', ' ': '/', "1": "•----", "2": "••---", "3": "•••--", "4": "••••-",
              "5": "•••••", "6": "-••••", "7": "--•••", "8": "---••", "9": "----•", "0": "-----", }


def code_to_morse(text_to_encode):
    output = ""
    text_to_encode = text_to_encode.split(" ")
    print(text_to_encode)
    for word in text_to_encode:
        for letter in word:
            try:
                output += morse_code[letter] + " "
            except KeyError:
                pass
    print(output)


def decode_from_morse(text_to_decode):
    output = ""
    text_to_decode = text_to_decode.split(" ")
    for letter in text_to_decode:
        for key, value in morse_code.items():
            if value == letter:
                output += key + " "
    print(output)


def start():
    choice1 = input("Type encode or decode: ").lower()
    if choice1 == "encode":
        text_to_encode = input("Please insert text you would like to encode: ")
        code_to_morse(text_to_encode)
    elif choice1 == "decode":
        text_to_decode = input("Please insert morse code you would like to decode: ")
        decode_from_morse(text_to_decode)
    else:
        print("Try again.")
        start()


start()
