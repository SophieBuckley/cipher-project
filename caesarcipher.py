#A simple function which takes a text input and an integer input and transforms the text input via the Caesar cipher method of encryption. 
#It can also decrypt messages which have previously been transformed.

prompt = raw_input("Would you like to encrypt or decrypt a message? ")

def encrypt_caesar(text, shift):

    result = ""

    #Traverse the text input.
    for i in range(len(text)):
        #Gets each letter in turn.
        char = text[i]
        #Checks whether the current character is alphanumeric.
        if char.isalnum() == True:
            #Change char to ordinal value.
            char = ord(char)
            if shift == shift % 26:
                #Apply cipher shift.
                char += shift
                #Change char back to a string value.
                char = chr(char)
                result += char
        else:
            result += char
    print result

def decrypt_caesar(text, shift):

    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isalnum() == True:
            char = ord(char)
            if shift == shift % 26:
                char -= shift
                char = chr(char)
                result += char
        else:
            result += char
    print result

def bruteforce_caesar(text):
    
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for key in range(len(letters)):
        result = ""
        text = text.upper()
        for symbol in text:
            if symbol in letters:
                num = letters.find(symbol)
                num -= key
                if num < 0:
                    num += len(letters)
                result += letters[num]
            else:
                result += symbol

        print("Key #%s: %s" % (key, result))

text = raw_input("Enter your message: ")

#If statement for user choice to encrypt or decrypt.
if prompt == "Encrypt" or prompt == "encrypt":
    shift = input("Enter your shift value: ")
    encrypt_caesar(text, shift)
elif prompt == "Decrypt" or prompt == "decrypt":
    prompt = raw_input("Do you know the key shift value? ")
    if prompt == "Yes" or prompt == "yes":
        shift = input("Enter your shift value: ")
        decrypt_caesar(text, shift)
    elif prompt == "No" or prompt == "no":
        bruteforce_caesar(text)
