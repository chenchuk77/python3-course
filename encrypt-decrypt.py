from random import shuffle

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

def decrypt(encrypted_text, key):
    output = encrypted_text
    print ("encrypted_text: {}".format(encrypted_text))
    p = get_probability()

    freqs = { letter:0 for letter in key }
    print(freqs)
    for letter in encrypted_text.lower():
        if letter in key:
            freqs[letter] += 1
    print(freqs)

    # sort both lists
    probs_values_list = list(p.values())
    probs_values_list.sort(reverse=True)

    for elem in probs_values_list:
        print (elem, '--', probs_values_list.index(elem), End=' ')

    my_values_list = list(p.values())
    my_values_list.sort(reverse=True)

    for i in range (26):
        output.replace(my_values_list[i], probs_values_list[i])
    return output

def get_probability():
    return {
        'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
        'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
        'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
        'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
        'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074}

t = 'hello'
t1 = """
Konta had never won a main-draw match at Roland Garros before this year and appears to be reaping the rewards of her work with coach Dimitri Zavialoff, whom she employed at the end of last year.
She is trusting her ability on a surface where she has had little previous success and against Vekic, this was again evident.
Konta produced 33 winners and seven aces on her way to victory, improving her tallies in these areas from each of her previous three matches.
Former world number four Konta was rarely flustered against Vekic, who she memorably beat in a three-set thriller on her way to the Wimbledon semi-finals two years ago.
After bouncing straight back from losing her opening service game, the Briton broke again for a 5-2 lead and kept a measure of calm to see off four break points before sealing the set with an ace down the middle.
Serve ruled at the start of the second set - with only eight receiving points won in the opening six games - before Konta struck first for a 4-3 advantage.
For the first time she wobbled as three unforced errors handed the break straight back, but she managed to reset again in the next game.
Two whopping forehands, which dusted the baseline, set the tone, forcing Vekic into a panicked backhand volley wide that brought up three break points for the Briton.
Vekic saved two of them, only for Konta to take the third when she pulled off an outrageous backhand drop shot from the back of the court.
Konta took her first match point when she expertly judged a Vekic return was going long, breaking out into a broad smile and raising both arms skywards in celebration.
"""
k = get_enc_key()
cipher = encrypt(t, k)
print (cipher)

clear = decrypt(cipher, k)
print (clear)

#print (t, k)

