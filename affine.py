import math

def affine_encrypt(plaintext, alpha, beta):
	text = plaintext.lower()
	text = text.replace(" ", "")

	if math.gcd(alpha, 26) != 1:
		return "Alpha must be co-prime to 26. Valid values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25"

	cipher = ""
	for char in text:
		val = alpha * (ord(char) - 97) + beta
		val = (val % 26) + 97

		cipher = cipher + chr(val)

	return cipher.upper()


def affine_decrypt(cipher, alpha, beta): 
	text = cipher.lower()
	
	if math.gcd(alpha, 26) != 1:
		return "Alpha must be co-prime to 26. Valid values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25"

	# Let alpha2 be the multiplicative inverse of alpha
	i = 1
	while (alpha*i) % 26 != 1:
		i += 1
	alpha2 = i

	plaintext = ""
	for char in text:
		val = alpha2 * ((ord(char) - 97) - beta)
		if val < 0: val + 26
		val = (val % 26) + 97
		plaintext += chr(val)

	return plaintext

# Test
# plaintext = input("Please enter your message: ")
# alpha, beta = map(int, input("Please enter the values for alpha and beta: ").split())

# while math.gcd(alpha, 26) != 1:
#   print("Invalid alpha. Acceptable values are: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25")
#   alpha = int(input("Please enter a valid alpha: "))

# # Call the functions
# res = affine_encrypt(plaintext, alpha, beta)
# print(res)