# Imports
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

localkeys = [ ]
message = " "



def rsakeygen(bitforce, namefile):
    global rsabackend, prkey, pukey, localkeys

    # Generate RSA pair of keys
    rsabackend = Random.new().read
    prkey = RSA.generate(bitforce, rsabackend)
    pukey = prkey.publickey()
    localkeys.append(prkey.export_key().decode())
    
    
    #print(localkeys)

    # Save two steps private keys for decryption
    with open(namefile, 'w') as f:
        for keys in localkeys:
            f.write(str(keys) + '\n')
    localkeys = [ ]




choise=input("Import the text to encrypt from a file or input? (y/n):  ")

if choise.lower() == 'y':
     print("Loading..")
     with open("secretext.txt", 'r') as f:
          message = f.read()
     print("Loaded")

else:
     # Enter the message to be encrypted
     message=input("Enter your text: ")
     




# Encrypt the message with two steps.
print("Genkey 1")
rsakeygen(4096, "rsa1.txt")
print("Generated")
cipher = PKCS1_OAEP.new(pukey)
encr1 = cipher.encrypt(message.encode())
print("Encrypted step 1")


print("Genkey 2")
rsakeygen(8196, "rsa2.txt")
print("Generated")
cipher = PKCS1_OAEP.new(pukey)
encr2 = cipher.encrypt(encr1)
print("Encrypted step 2")

# Save the secret text {already encrypted}
print("Saving..")
with open("secret.txt", 'w') as f:
        f.write(str(encr2))


print(encr2)
print("Saved!")
