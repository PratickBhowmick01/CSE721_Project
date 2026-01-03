import math

def hillMatrix(key):
	arr = list(map(int, key.split()))
	matrix = [[arr[0], arr[1]], [arr[2], arr[3]]]

	return matrix

def hill_encrypt(plaintext, matrix):
	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
	determinant = a*d - b*c
	while determinant < 0: determinant += 26
	determinant %= 26

	if math.gcd(determinant, 26) != 1:
		return "Please enter a valid matrix. GCD of the determinant(M) and 26 must be 1"

	text = plaintext.lower()
	text = text.replace(" ", "")
	if len(text) % 2 != 0: text += 'z'
	
	arr = []
	for i in range(0, len(text)):
		val = ord(text[i]) - 97
		arr.append(val)

	cipher = ""
	for i in range(0, len(arr), 2):
		val1, val2 = arr[i], arr[i+1]

		res1, res2 = val1*a + val2*c, val1*b + val2*d
		res1, res2 = (res1 % 26) + 97, (res2 % 26) + 97
		
		cipher += chr(res1) + chr(res2)
	
	return cipher.upper()


def hill_decrypt(cipher, matrix):
	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
	determinant = a*d - b*c
	while determinant < 0: determinant += 26
	determinant %= 26

	if math.gcd(determinant, 26) != 1:
		return "Please enter a valid matrix. GCD of the determinant(M) and 26 must be 1"
	
	text = cipher.lower()

	i = 1
	while determinant*i % 26 != 1:
		i += 1

	inv_matrix = [[d, -b], [-c, a]]
	for j in range(2):
		for k in range(2):
			inv_matrix[j][k] *= i

			while inv_matrix[j][k] < 0: inv_matrix[j][k] += 26
			inv_matrix[j][k] %= 26
	a, b, c, d = inv_matrix[0][0], inv_matrix[0][1], inv_matrix[1][0], inv_matrix[1][1]

	arr = []
	for i in range(0, len(text)):
		val = ord(text[i]) - 97
		arr.append(val)

	plaintext = ""
	for i in range(0, len(arr), 2):
		val1, val2 = arr[i], arr[i+1]

		res1, res2 = val1*a + val2*c, val1*b + val2*d
		res1, res2 = (res1 % 26) + 97, (res2 % 26) + 97
		
		plaintext += chr(res1) + chr(res2)
	
	return plaintext


# Test run
# key = input("Please enter the matrix: ")
# matrix = hillMatrix(key)

# ciphertext = hill_encrypt("kokil", matrix)
# plaintext = hill_decrypt(ciphertext, matrix)

# print("Cipher: {ciphertext} Plaintext: {plaintext}".format(ciphertext=ciphertext, plaintext=plaintext))