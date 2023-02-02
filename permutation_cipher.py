import itertools
from utiilities import convert_letter_to_number, convert_number_to_letter

with open('encrypted_ciphers/ciphertext1.txt', 'r') as file:
    ciphertext = file.read()  

# key can range from 3 to 10, so start at 3
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
    # divided_string_number = ' '.join(map(str, divided_string_number))
    cipher_numbers.append(divided_string_number)
    divided_string_number = []


permutations = []
def permutations(key):
    decrypted_word = []
    deciphered_text = ""
    numbers = list(range(1, key + 1))
    permutations = list(itertools.permutations(numbers))
    # for permutation in permutations:
    #     print(permutation)
    #     if permutation == [6,1,9,3,2,0,8,4,5,7]:
    #         print("Here we go")
    #     if permutation == [1,2,3,4,5,6,8,7,9,10]:
    #         print("Here we go")
    #     # example: [3, 2, 1]
    #     permutation = list(permutation)
    #     # print("\npermutation {}:".format(permutation))
    #     num = 0
    permutation = [6,1,9,3,2,0,8,4,5,7]
    for cipher_number in cipher_numbers:
        # num += 1
        # permutated_list = [cipher_number[i] for i in permutation if i <= len(cipher_number)]
        permutated_list = [cipher_number[i] for i in permutation if i < len(cipher_number)]
        for p in permutated_list:
            if isinstance(p, int):
                print(convert_number_to_letter(p))
        for number in permutated_list:
            if isinstance(number, int):
                number = convert_number_to_letter(number)
            decrypted_word.append(number)
        deciphered_text += "".join(decrypted_word)
        decrypted_word = []
    file = open("decrypted_ciphers/decrypted_cipher1.txt", "w")
    file.write(deciphered_text)
    file.close()
    deciphered_text = ""
                      
# Example usage for key = 3
permutations(key_length)