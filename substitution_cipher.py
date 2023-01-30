permutation_dict = {
    'a': 'L', 'b': 'K','c': 'J','d': 'H','e': 'G','f': 'F','g': 'D','h': 'S','i': 'A','j': 'I','k': 'W',
    'l': 'E','m': 'R','n': 'T','o': 'Y','p': 'U','q': 'Q','r': 'O','s': 'P','t': 'Z','u': 'X','v': 'C',
    'w': 'V','x': 'B','y': 'N','z': 'M'
}

with open('encrypted_ciphers/ciphertext2.txt', 'r') as file:
    ciphertext = file.read()  

for letter in ciphertext:
    if letter.isalpha():
        ciphertext = ciphertext.replace(letter, list(permutation_dict.keys())[list(permutation_dict.values()).index(letter)])
    
file = open("decrypted_ciphers/decrypted_cipher2.txt", "w")
file.write(ciphertext)
file.close()