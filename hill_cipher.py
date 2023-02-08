with open('encrypted_ciphers/ciphertext4.txt', 'r') as file:
    ciphertext = file.read()
    
# by visualizing the text, we can see that SVC refer refer to the, but also
# FNM refer to the. And we see many SV and NM repeating in different places. 
# For Hill cipher, the encrypted letter depends also on its neighbor
# for the (SVC) has S and V as t and h. However, the (FNM) has N and M as h and e.
# e(t, h) = (S, V)
# e(h, e) = (N, M)

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


x = [(19, 7), (7, 4)]
x_inverse = inverse_matrix_mod_26(x)

x_inverse = [(x_inverse[0], x_inverse[1]), (x_inverse[2], x_inverse[3])]
y = [(18, 21), (13, 12)]

key = multiply_matrices_mod_26(x_inverse, y)

print("Key:")
for row in key:
    print("{:>2} {:>2}".format(row[0], row[1]))