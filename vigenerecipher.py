#A function which performs the vigenere encryption algorithm on an input phrase.

key = raw_input("Please enter the keyword that you would like to use for your encryption: ")
message = raw_input("Please enter the message that you would like to encrypt: ")

def encrypt_vigenere(key, message):

    #Empty list to host results.
    result = []
    #Index to be used to cycle through letters.
    alphabet_index = 0

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Convert key input to all uppercase letters.
    key = key.upper()
    #For every letter in the message...
    for symbol in message:
        #... convert to uppercase version and find it's counterpart in the 'letters' list.
        num = letters.find(symbol.upper())
        #If this counterpart is not found (i.e. the input key is longer than 26 letters)...
        if num != (-1):
            #... cycle to the start of 'key'...
            key_index = alphabet_index % len(key)
            num += letters.find(key[key_index])
            #... and cycle to the start of letters to continue assignment.
            num = num % len(letters)
    
            if symbol.isupper():
                result.append(letters[num])
            elif symbol.islower():
                result.append(letters[num].lower())

            print symbol, key[key_index], letters[num]

        alphabet_index += 1
    
    #Print all of the list items in 'letters' as a string.
    print "".join(result)

encrypt_vigenere(key, message)
