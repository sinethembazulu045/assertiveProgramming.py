  
# This Dictionary shows the morse code chat
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}
# fuction for converting letters to morse code  
def lettersToMorseCode(message):
    morse_code = ''
    message =message.upper()
    for letter in message: 
        if letter != ' ':  
            morse_code += MORSE_CODE_DICT[letter] + ' '
        else: 
            morse_code+= ' '         
    return morse_code


def morseCodeToLetters(message): 
  
    # extra space added at the end to access the 
    # last morse code 
    message += ' '
    englishLetters = '' 
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
            if i == 2 : 
                 # adding space to separate words 
                englishLetters += ' '
            else: 
  
                # accessing the keys using their values (reverse of encryption) 
                englishLetters += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT .values()).index(citext)] 
                citext = '' 
    return englishLetters


def main():
   message1 = "Hi there"
   output1 = lettersToMorseCode(message1.upper())
   print (output1)
   message2 = ".... ..  - .... . .-. ."
   output2 = morseCodeToLetters(message2)
   assert output2 == output1, "English latters should match with its merso code"
   print (output2)
# Executes the main function
if __name__ == '__main__':
   main()