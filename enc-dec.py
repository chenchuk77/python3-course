from random import shuffle

def get_ordered_letters_list(p):
    ''' accepts a dictionary of probabilities and returns a sorted list 
    of letters ordered by prob where list[0] is the highest probability '''
    # sort the values
    pvalues = list(p.values())
    pvalues.sort(reverse=True)
    pvalues
    # extract the keys (letters) and add 1 letter each iteration
    letters = []
    for v in pvalues:
        letters += [letter for letter, prob in p.items() if prob == v ]
    return letters

def get_probability_dataset():
    return {
        'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
        'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
        'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
        'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
        'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074}

def get_enc_key():
    abc_list =  [ chr(97 + i) for i in range(26)]
    k = abc_list
    shuffle(k)
    return k

def encrypt(clear_text, key):
    #print ("clear: {}".format(clear_text))
    cipher = ''
    for letter in clear_text.lower():
        if letter in key:
            pos = ord(letter)-97
            enc_letter = key[pos]
            #print (letter, pos, enc_letter)
            cipher += enc_letter
        else:
            cipher += letter
    return cipher

# loads the dataset
p = get_probability_dataset()
clear_text = 'hello'

# encryption
k = get_enc_key()
enc_text = encrypt(clear_text, k)
print ('clear: ', clear_text)
print ('encrypted: ', enc_text)

# decryption
letters = get_ordered_letters_list(p)
print ('letters: ', letters, end = ' ')
