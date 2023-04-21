# Imports
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast


key1 = " "
key2 = " "
encrtxt = " "

# Import all keys and the text.
with open("rsa1.txt", "r") as f:
    key1 = f.read()

with open("rsa2.txt", "r") as f:
    key2 = f.read()

with open("secret.txt", "r") as f:
    encrtxt = f.read()

encrtxt = ast.literal_eval(encrtxt)

#print(encrtxt)
#print(key1)
#print(key2)

# Import keys on RSA decryptor and decrypt the text.
rsa2key = RSA.importKey(key2)
cipher2 = PKCS1_OAEP.new(rsa2key)
decrtxt = cipher2.decrypt(encrtxt)

rsa1key = RSA.importKey(key1)
cipher1 = PKCS1_OAEP.new(rsa1key)
decrtxt2 = cipher1.decrypt(decrtxt)

print(decrtxt2)

# Save the result in a file.
with open("decryptedtext.txt", 'w') as f:
        f.write(str(decrtxt2))
