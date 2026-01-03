import string

def playMatrix(key):
  key = key.lower()
  key = key + string.ascii_lowercase

  flag = False
  key2 = ""
  for char in key:
    if char not in key2:
      if char in 'ij' and flag == False:
        flag = True
      elif char in 'ij' and flag:
        continue
      key2 = key2 + char

  matrix = [[0 for j in range(5)] for i in range(5)]
  k = 0
  for i in range(5):
    for j in range(5):
      matrix[i][j] = key2[k]
      k += 1

  return matrix


def playfair_encrypt(plaintext, matrix):
  temp = plaintext.lower()
  temp = temp.replace(" ", "")

  text = ""
  i = 0
  while i < len(temp)-1:
    if temp[i] != temp[i+1]:
      text = text + temp[i:i+2]
    else:
      text = text + temp[i] + 'z' + temp[i+1] + temp[i+2]
      i += 1

    i += 2
    if i == len(temp)-1:
      text += temp[i] + 'z'

  cipher = ""
  for i in range(0, len(text) - 1, 2):
    a, b = text[i], text[i+1]
    r1,r2,c1,c2 = 0, 0, 0, 0

    for j in range(5):
      for k in range(5):
        if matrix[j][k] == a:
          r1,c1 = j,k
        if matrix[j][k] == b:
          r2,c2 = j,k
   
    if r1 == r2:
      cipher += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2:
      cipher += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:
      cipher += matrix[r1][c2] + matrix[r2][c1]

  return cipher.upper()


def playfair_decrypt(cipher, matrix):
  text = cipher.lower()

  plaintext = ""
  for i in range(0, len(text) - 1, 2):
    a, b = text[i], text[i+1]
    r1,r2,c1,c2 = 0, 0, 0, 0

    for j in range(5):
      for k in range(5):
        if matrix[j][k] == a:
          r1,c1 = j,k
        if matrix[j][k] == b:
          r2,c2 = j,k

    if r1 == r2:
      plaintext += matrix[r1][c1-1] + matrix[r2][c2-1]
    elif c1 == c2:
      plaintext += matrix[r1-1][c1] + matrix[r2-1][c2]
    else:
      plaintext += matrix[r1][c2] + matrix[r2][c1]

  return plaintext

# key = input("Please enter your key: ")
# plaintext = input("Please enter your text: ")

# matrix = playMatrix(key)
# cipher = playfair_encrypt(plaintext,matrix)
# print("Cipher:", cipher)

# print("After decryption:", plaintext)
