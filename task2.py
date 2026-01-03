import math

def task(plain, cipher):
	plain, cipher = plain.lower(), cipher.lower()
	plain_lst, cipher_lst = [], []
	
	for i in range(len(plain)):
		val1 = ord(plain[i]) - 97
		val2 = ord(cipher[i]) - 97

		plain_lst.append(val1)
		cipher_lst.append(val2)

	# Check if inverse matrix is possible.
	det = 0
	flag = False
	i,a,b,c,d = 0, 0, 0, 0, 0
	while i < len(plain_lst)-4:
		a,b,c,d = plain_lst[i], plain_lst[i+1], plain_lst[i+2], plain_lst[i+3]
		det = a*d - b*c
		while det < 0: det += 26
		det %= 26

		if math.gcd(det, 26) == 1: 
			flag = True 
			break
		i += 4

	if flag == False:
		print("Data insufficient to break the cipher")
		return
	
	# Compute the inverse matrix of P
	inv = 1 
	while (det*inv) % 26 != 1:
		inv += 1

	inv_p = [[d,-b], [-c,a]]
	for x in range(2):
		for y in range(2):
			inv_p[x][y] *= inv

			while inv_p[x][y] < 0: inv_p[x][y] += 26
			inv_p[x][y] %= 26
	# print(inv_p)

	# Computing the key, K = P^-1 * C
	c = [[cipher_lst[i], cipher_lst[i+1]], [cipher_lst[i+2], cipher_lst[i+3]]]
	key = [[0,0], [0,0]]

	for x in range(2):
		for y in range(2):
			key[x][y] = ( inv_p[x][0]*c[0][y] + inv_p[x][1]*c[1][y] ) % 26
	
	print("The key is:")
	for x in range(2):
		for y in range(2):
			print(key[x][y], end = " ")
		print()

plaintext = input("Please enter the plaintext: ")
ciphertext = input("Please enter the ciphertext: ")
task(plaintext, ciphertext)


'''
Sample: plain-help; cipher-ZEBB
plain: helloworld; cipher-ZQIRCWVHCT	| 5 8 17 3
'''