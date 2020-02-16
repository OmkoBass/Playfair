def playfair(word, key):
    c = 0

    matrix = [[0 for x in range(5)] for y in range(5)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if c in range(len(key)):
                matrix[i][j] = key[c]
                try:
                    alphabet.remove(key[c])
                except:
                    continue
                c += 1

    c = 0

    for i in range(len(matrix)):
        for j in range (len(matrix)):
            if matrix[i][j] == 0:
                matrix[i][j] = alphabet[c]
                c += 1

    print('\n*****PLAYFAIR SQUARE*****')
    for row in matrix:
        print(row)

    word = split_even(word, 2)    

    word = transform_word(matrix, word)

    print(f'\nThe transformed text is: {word}')

def transform_word(matrix, word):
    i = 0
    index = []
    ciphered = []

    while i < len(word):
        index.append(location(matrix, word[i]))
        i += 1

    for i in range(0, len(index) - 1, 2):
        ciphered.append((ciphered_letter(index[i], index[i+1], matrix)))

    return ciphered

def location(matrix, letter):
    #Return the location of the letter
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == letter:
                return (i,j)

def ciphered_letter(pos1, pos2, matrix):
    if pos1[0] == pos2[0]:
        #Same row
        return (matrix[pos1[0]][(pos1[1]+1) % 5], matrix[pos2[0]][(pos2[1]+1) % 5])
    if pos1[1] == pos2[1]:
        #Same column
        return (matrix[(pos1[0]+1) % 5][pos1[1]], matrix[(pos2[0]+1) % 5][pos2[1]])
    else:
        return (matrix[pos1[0]][pos2[1]], matrix[pos2[0]][pos1[1]])

def split_even(word, n):
    #Splits words evenly, adds X if needed and removes whitespace
    words = []

    for val in chunks(word, 2):
        words.extend(val)

    if len(words) % 2 == 1:
        words.extend('X')

    return words

def chunks(list, n):
    for i in range(0, len(list), n):
        yield list[i:i + n]

def fix_word_key(val):
    val = val.upper()
    val = val.replace('J', 'I')
    val = val.replace(' ', '')

    return val

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = input('Enter the word you want to cipher: ')
word = fix_word_key(word)

key = input('Enter your key: ')
key = fix_word_key(key)

#Removed the duplicates but preserves the order
distinct = []
[distinct.append(letter) for letter in key if letter not in distinct]

playfair(word, distinct)
