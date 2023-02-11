from utiilities import convert_letter_to_number, convert_number_to_letter, inverse_matrix_mod_26, multiply_matrices_mod_26

with open('encrypted_ciphers/ciphertext4.txt', 'r') as file:
    ciphertext = file.read()

ciphertext = ciphertext.replace(",", "")
ciphertext = ciphertext.replace(".", "")
ciphertext = ciphertext.replace("-", " ")
ciphertext = ciphertext.replace("\n", "")
ciphertext = ciphertext.replace("'", "")
ciphertext = ciphertext.replace('"', '')
ciphertext = ciphertext.replace('(', '')
ciphertext = ciphertext.replace(')', '')

punctuation = []
for i in range(len(ciphertext)):
    if ciphertext[i] == " ":
        punctuation.append(i)


ciphertext = ciphertext.replace(" ", "")
    
# by visualizing the text, we can see that SVC refer refer to the, but also
# FNM refer to the. And we see many SV and NM repeating in different places. 
# For Hill cipher, the encrypted letter depends also on its neighbor
# for the (SVC) has S and V as t and h. However, the (FNM) has N and M as h and e.
# e(t, h) = (S, V)
# e(h, e) = (N, M)

key = [(7, 0), (17, 3)]
key_inverse = inverse_matrix_mod_26(key)

key_inverse = [(key_inverse[0], key_inverse[1]), (key_inverse[2], key_inverse[3])]

last_letters = 4 - (len(ciphertext) % 4)
if len(ciphertext) % 4 != 0:
    for i in range((4 - (len(ciphertext) % 4))):
        ciphertext += " "

i = 0
to_decypher_letters = []
y = []
plaintext = []
for cipher in ciphertext:
    to_decypher_letters.append(cipher)
    # make sure it is 4 letters at a time
    if i == 3:
        for letter in to_decypher_letters:
            y.append(convert_letter_to_number(letter))
        y = [(y[0], y[1]), (y[2], y[3])]
        x = multiply_matrices_mod_26(y, key_inverse)
        x = sum(x, [])
        for decyphered_number in x:
            plaintext.append(convert_number_to_letter(decyphered_number))
        y = []
        to_decypher_letters = []
        i = 0
    else:
        i += 1


plaintext = ' '.join(plaintext).replace(" ", "")

for i in range(len(punctuation)):
    for j in range(len(plaintext)):
        if j == punctuation[i]:
            plaintext = plaintext[:j] + ' ' + plaintext[j:]

plaintext = plaintext[:-last_letters]

file = open("decrypted_ciphers/decrypted_cipher4.txt", "w")
file.write(plaintext)
file.close()