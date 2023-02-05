import itertools
from utiilities import convert_letter_to_number, convert_number_to_letter

with open('encrypted_ciphers/ciphertext1.txt', 'r') as file:
    ciphertext = file.read()  

ciphertext = ciphertext.replace(" ", "")
ciphertext = ciphertext.replace(",", "")
ciphertext = ciphertext.replace(".", "")
ciphertext = ciphertext.replace("-", "")
ciphertext = ciphertext.replace("\n", "")
ciphertext = ciphertext.replace("'", "")
ciphertext = ciphertext.replace('"', '')
# key can range from 3 to 10
key_length = 10

def divide_string(string, key_length):
    return [string[i:i + key_length] for i in range(0, len(string), key_length)]

divided_ciphertext = divide_string(ciphertext, key_length)

divided_string_number = []
cipher_numbers = []
for divided_string in divided_ciphertext:
    for letter in divided_string:
        if letter.isalpha():
            letter = convert_letter_to_number(letter)
        divided_string_number.append(letter)
    cipher_numbers.append(divided_string_number)
    divided_string_number = []


permutations = []
def permutations(key):
    decrypted_word = []
    deciphered_text = ""
    numbers = list(range(1, key + 1))
    permutations = list(itertools.permutations(numbers))
    # no matches with the first half, try second half
    second_half = permutations[len(permutations)//2:]
    for permutation in second_half:
        permutation = list(permutation)
        num = 0
        for cipher_number in cipher_numbers:
            num += 1
            permutated_list = [cipher_number[i] for i in permutation if i < len(cipher_number)]
            for number in permutated_list:
                if isinstance(number, int):
                    number = convert_number_to_letter(number)
                decrypted_word.append(number)
            deciphered_text += "".join(decrypted_word)
            decrypted_word = []
        if "enigma" in deciphered_text and "germany" in deciphered_text and "mathematicians" in deciphered_text and "cryptologic" in deciphered_text and "alliesfavortheend" in deciphered_text:
            print("\npermutation {}:".format(permutation))
            file = open("decrypted_ciphers/decrypted_cipher1.txt", "w")
            file.write(deciphered_text)
            file.close()
        deciphered_text = ""
                      
# Example usage for key = 3
permutations(key_length)