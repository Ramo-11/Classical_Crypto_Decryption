import math

from utiilities import convert_letter_to_number, convert_number_to_letter, inverses, alph_prob

word_dict = {}
sorted_word_dict = {}

def find_letters_repition(ciphetext):
    global word_dict
    global sorted_word_dict
    ciphetext = ciphetext.lower()
    for letter in ciphetext:
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


with open('encrypted_ciphers/ciphertext6.txt', 'r') as file:
    original_ciphertext = file.read()    
find_letters_repition(original_ciphertext)
print(sorted_word_dict)

a, b = 0, 0
ciphertext = original_ciphertext
for i in range(len(sorted_word_dict.keys())):
    for j in range(1, len(sorted_word_dict.keys())):
        ciphertext = original_ciphertext
        if not list(sorted_word_dict.keys())[i].isalpha():
            break
        if not list(sorted_word_dict.keys())[j].isalpha():
            continue
        a, b = find_key(decrypted_letter_1=convert_letter_to_number(list(alph_prob.keys())[i]), encrypted_letter_1=convert_letter_to_number(list(sorted_word_dict.keys())[i]), 
                        decrypted_letter_2=convert_letter_to_number(list(alph_prob.keys())[i+1]), encrypted_letter_2=convert_letter_to_number(list(sorted_word_dict.keys())[j]))
        print("equation 1: {} -> {}".format(list(sorted_word_dict.keys())[i].upper(), list(alph_prob.keys())[i]))
        print("equation 2: {} -> {}".format(list(sorted_word_dict.keys())[j].upper(), list(alph_prob.keys())[i+1]))
        if a == 0 and b == 0:
            print("Could not find key\n")
        else:
            print("key = ({}, {})\n".format(a, b))
            for encrypted_letter in ciphertext:
                if not encrypted_letter.isalpha():
                    continue
                num = (inverses.get(a)*(convert_letter_to_number(encrypted_letter)-b)) % 26
                decrypted_letter = convert_number_to_letter(num)
                ciphertext = ciphertext.replace(encrypted_letter, decrypted_letter)
            f = open("decrypted_ciphers/decrypted_cipher6.txt", "w")
            f.write(ciphertext)
            f.close()
            if "the" in ciphertext and "and" in ciphertext:
                print("found")
                exit()