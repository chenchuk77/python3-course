from random import shuffle

def get_ordered_values_list(d):
    ''' accepts a dictionary of and returns a list of keys, sorted by
    the corresponding value in dict (ie. list[0] is the key of the highest value) '''
    # sort the values
    dvalues = list(d.values())
    dvalues.sort(reverse=True)
    # extract the keys (letters) and add 1 letter each iteration
    keys = []
    for v in dvalues:
        keys += [key for key, val in d.items() if val == v ]
    return keys

def get_probability_dataset():
    ''' a given dataset of a-z probabilities '''
    return {
        'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
        'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
        'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
        'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
        'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074}

def get_enc_key():
    '''  returns a random ordered list of all small letters a-z '''
    abc_list =  [ chr(97 + i) for i in range(26)]
    k = abc_list
    shuffle(k)
    return k

def encrypt(clear_text, key):
    '''  replace each letter with the corresponding index in the key.('a' replaced by key[0]) '''
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

def decrypt(encrypted_text, key):
    '''  count letter appearances in encrypted-text and replace each letter with the matching probability '''
    # loads the dataset of probabilities 
    p = get_probability_dataset()
    output = ''
    
    # init a dict to count letters appearnces in the encrypted text
    counts = { letter:0 for letter in key }
    for letter in encrypted_text.lower():
        if letter in key:
            counts[letter] += 1

    # sort both lists such as p_list[0] is the most probable letter (by dataset)
    # and c_list[0] is the letter with the most count 
    p_list = get_ordered_values_list(p)
    c_list = get_ordered_values_list(counts)

    # build the output string by switch known english letters and preserve the rest
    for letter in enc_text:
        if letter in c_list:
            # append letter with same index from the probability list
            output += p_list[c_list.index(letter)]
        else:
            output += letter
    return output

dec_text=''
enc_text=''
k = ''
 
#clear_text = 'hello'
print ('clear_text: {}'.format(clear_text)[:40])

# encryption
k = get_enc_key()
enc_text = encrypt(clear_text, k)
#print ('clear: ', clear_text)
print ('encrypted: {}'.format(enc_text)[:40])

# decryption
#letters = get_ordered_letters_list(p)
#print ('letters: ', letters, end = ' ')
dec_text = decrypt(enc_text, k)
print ('decrypted: {}'.format(dec_text)[:40])
