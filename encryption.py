import random
import string

chars= " "+string.punctuation+ string.ascii_letters+ string.digits
# print(chars)

chars=list(chars)
keys=chars.copy()
random.shuffle(keys)
#string copy

print(f"chars:{chars}")
print(f"keys:{keys}")

#Encryption
user_text=input("Enter the text you want to encrypt")
cipher_text=""

for letter in user_text:
    index =chars.index(letter)
    cipher_text+=keys[index]

print(f"Original message: {user_text}")
print(f"Encrypted message: {cipher_text}")

#Decryption
ciphered_txt= input("Enter the text to decrypt")
plain_text=""

for letter in ciphered_txt:
    index= keys.index(letter)
    plain_text+=chars[index]

print(f"Decrypted message: {ciphered_txt}")
print(f"Original message: {plain_text}")