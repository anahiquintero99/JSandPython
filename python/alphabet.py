def listAlphabet(pangram):
    AlphabetLowerCase =  list(map(chr, range(97, 123)))
    AlphabetUpperCase = list(map(chr, range(65, 90)))
    print(pangram)
    for letter in AlphabetLowerCase or AlphabetUpperCase:
        if letter not in pangram:
            print('False')

    print('True')

pangram = "The quick, brown fox jumps over the lazy dog!"
listAlphabet(pangram)