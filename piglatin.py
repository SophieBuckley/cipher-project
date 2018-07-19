#Whilst Pig Latin isn't a cipher per say, it is a method of 'encrypting' words, so I thought I would create this for fun.

message = raw_input('Please enter your message: ')

def pig_latin(message):

    words = []
    piglatin = []
    vowels = ('a','e','i','o','u')
    result = ''
    
    #Splits the input string into a list of elements and assigns it to words.
    words = message.split()

    #For each word in the list words...
    for word in words:
        #If the length of the word is more than one (i.e. not 'a' or 'I')...
        if len(word) > 1:
            #If the word starts with a vowel, just add 'yay' to the end of the word.
            if word.startswith(vowels):
                word += 'yay'
                piglatin.append(word)
            #If the word starts with a consonant, move the first letter to the end and then add 'ay'.
            elif word[0] != vowels and word[1] == vowels:
                letter =  word[0]
                word += letter + 'ay'
                #Append everything after the first letter of the word to 'piglatin', i.e. 'greengay', 'reengay' is appended.
                piglatin.append(word[1:])
            #If the word starts with a consonant cluster (e.g. smile), append everything after the second letter and then add 'ay'.
            elif word[0] != vowels and word[1] != vowels:
                letter = word[0] + word[1]
                word += letter + 'ay'
                #Append everything after the second character in the string.
                piglatin.append(word[2:])
        else:
            piglatin.append(word)

    #Join the list of strings together to form one string.
    result = ' '.join(piglatin)
    print result

pig_latin(message)
