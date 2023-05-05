MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '': ''}


def decodeMorse(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return decipher

def main():
    code = input("Input the Morse code to translate\nPress 'C' if you want to see Morse Code Dictionary\nPress 'E' to exit:\n").capitalize()

    if code == 'C':
        print("\n")
        for x in MORSE_CODE_DICT:
            print(f"{x} : {MORSE_CODE_DICT[x]}\n")
        main()
    elif code == 'E':
        exit
    elif code == '':
        print("\nPress 'E' to exit.\n")
        main()
    else:
        print(decodeMorse(code))
        main()
    

if __name__=="__main__":
    main()