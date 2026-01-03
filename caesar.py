def caesar_encrypt(plaintext, key):
  text = plaintext.lower()
  text = text.replace(" ", "")

  cipher = ""
  for char in text:
    val = ord(char) + key
    if val > 122: val -= 26

    cipher = cipher + chr(val)

  return cipher.upper()


def caesar_decrypt(cipher, key):
  text = cipher.lower()
  text = text.replace(" ", "")

  plaintext = ""
  for char in text:
    val = ord(char) - key
    if val < 97: val += 26

    plaintext += chr(val)

  return plaintext