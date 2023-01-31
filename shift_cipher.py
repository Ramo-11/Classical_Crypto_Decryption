from utiilities import convert_letter_to_number, convert_number_to_letter

with open('encrypted_ciphers/ciphertext5.txt', 'r') as file:
    original_ciphertext = file.read()  

ciphertext = original_ciphertext
key = 0
while "the" not in ciphertext:
    ciphertext = original_ciphertext
    key += 1
    for letter in ciphertext:
        if letter.isalpha():
            encrypted_letter_num = convert_letter_to_number(letter)
            decrypted_letter_num = (encrypted_letter_num - key) % 26
            ciphertext = ciphertext.replace(letter, convert_number_to_letter(decrypted_letter_num))
    
print("key is: {}".format(key))

file = open("decrypted_ciphers/decrypted_cipher5.txt", "w")
file.write(ciphertext)
file.close()