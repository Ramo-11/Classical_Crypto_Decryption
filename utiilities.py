alph_prob = {'e': 0.127, 't': 0.091, 'a': 0.082, 'o': 0.075, 'i': 0.07, 'n': 0.067, 's': 0.063, 'h': 0.061, 'r': 0.06, 'd': 0.043, 
            'l': 0.04, 'c': 0.028, 'u': 0.028, 'm': 0.024, 'w': 0.024, 'f': 0.022, 'g': 0.02, 'y': 0.02, 'p': 0.019, 'b': 0.015, 
            'v': 0.01, 'k': 0.008, 'j': 0.001, 'q': 0.001, 'x': 0.001, 'z': 0.001}
    
inverses = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}
    
def convert_letter_to_number(letter):
    return ord(letter.lower()) - ord('a')


def convert_number_to_letter(num):
    return chr(num + ord('a'))


def mod_26_inverse(a, b, c, d):
    det = (a*d - b*c) % 26
    det_inv = 0
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break
    return (d * det_inv) % 26, (-b * det_inv) % 26, (-c * det_inv) % 26, (a * det_inv) % 26


def inverse_matrix_mod_26(x):
    a, b = x[0]
    c, d = x[1]
    return mod_26_inverse(a, b, c, d)


def multiply_matrices_mod_26(matrix1, matrix2):
    a, b = matrix1[0]
    c, d = matrix1[1]
    p, q = matrix2[0]
    r, s = matrix2[1]
    return [(a*p + b*r) % 26, (a*q + b*s) % 26], [(c*p + d*r) % 26, (c*q + d*s) % 26]