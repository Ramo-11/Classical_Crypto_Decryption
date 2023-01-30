import math
import time

word_dict = {}
sorted_word_dict = {}
alph_prob = {'e': 0.127, 't': 0.091, 'a': 0.082, 'o': 0.075, 'i': 0.07, 'n': 0.067, 's': 0.063, 'h': 0.061, 'r': 0.06, 'd': 0.043, 
            'l': 0.04, 'c': 0.028, 'u': 0.028, 'm': 0.024, 'w': 0.024, 'f': 0.022, 'g': 0.02, 'y': 0.02, 'p': 0.019, 'b': 0.015, 
            'v': 0.01, 'k': 0.008, 'j': 0.001, 'q': 0.001, 'x': 0.001, 'z': 0.001}
    
inverses = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}
    
def convert_letter_to_number(letter):
    return ord(letter.lower()) - ord('a')


def convert_number_to_letter(num):
    return chr(num + ord('a'))


def find_letters_repition(plaintext):
    global word_dict
    global sorted_word_dict
    plaintext = plaintext.lower()
    for letter in plaintext:
        if letter in word_dict.keys():
            prev_value = word_dict.get(letter)
            new_value = prev_value + 1
            word_dict.update({letter: new_value})
        else:
            word_dict.update({letter: 1})
    sorted_word_dict = dict(sorted(word_dict.items(), reverse=True, key=lambda x: x[1]))
    

def find_key(decrypted_letter_1, encrypted_letter_1, decrypted_letter_2, encrypted_letter_2):
    a = 1
    while a != 26:
        if math.gcd(a, 26) == 1:
            for b in range(26):
                if (decrypted_letter_1*a + b) % 26 == encrypted_letter_1 and (decrypted_letter_2*a + b) % 26 == encrypted_letter_2:
                    return (a, b)
        a += 1
    return (0, 0)


# with open('ciphertext2.txt', 'r') as file:
#     ciphertext = file.read()    
ciphertext = "FMXVEDKAPHFERBNDKRXRSREFNORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH"
find_letters_repition(ciphertext)
print(sorted_word_dict)

a, b = 0, 0
for char in sorted_word_dict:
    for other_char in sorted_word_dict:
        if not char.isalpha():
            break
        if not other_char.isalpha():
            continue
        a, b = find_key(decrypted_letter_1=4, encrypted_letter_1=convert_letter_to_number(char), decrypted_letter_2=19, encrypted_letter_2=convert_letter_to_number(other_char))
        if a == 0 and b == 0:
            print("Could not find key for equation one letter: {}, equation 2 letter: {}".format(char, other_char))
        else:
            print("key = ({}, {})".format(a, b))
            print("for equation one letter: {}, equation 2 letter: {}".format(char, other_char))
            for encrypted_letter in ciphertext:
                if not encrypted_letter.isalpha():
                    continue
                num = (inverses.get(a)*(convert_letter_to_number(encrypted_letter)-b)) % 26
                decrypted_letter = convert_number_to_letter(num)
                ciphertext = ciphertext.replace(encrypted_letter, decrypted_letter).upper()
            f = open("break_affine.txt", "w")
            f.write(ciphertext)
            f.close()
            # time.sleep(1)
            # with open('ciphertext1.txt', 'r') as file:
            #     ciphertext = file.read()