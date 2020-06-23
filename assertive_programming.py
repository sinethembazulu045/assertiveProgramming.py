#suppose the following dictionary shows morse code for each charectors difined below
CODE = { 'A':'.-', 'B':'-...', 
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

def text_to_morsecode(message): # function that converts text to morse code
    message =message.upper()       # incase we have small charecters, we convert them into Capital lettrs
    encoded_message= " "       # declaring empty string
    for character in message:    # looping for each charector in given text to covert into morse code
        if character != " ":
            encoded_message += CODE[character] + " "
        else:
            encoded_message = " " 
    return encoded_message


inv_code = {v:k for k,v in CODE.items()}
testCode = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"

def morsecode_to_text(message):
    messageSeparated = message.split(' ')
    decode_message = ''
    for character in messageSeparated:
        if character in inv_code:
            decode_message += inv_code[character]
        else:
            decode_message += ' '
    return decode_message

print(text_to_morsecode("Hi There"))
print(morsecode_to_text(".... .. / - .... . .-. ."))



