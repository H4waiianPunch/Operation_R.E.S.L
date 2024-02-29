# Importing RSA
from Crypto.PublicKey import RSA

# Importing a cipher thing needed for encryption/decryption
from Crypto.Cipher import PKCS1_OAEP

# Converts binary data to hex. No idea why we need this. Maybe we don't?
from binascii import hexlify

# Base64 for displaying the encrypted data in a txt file?
import base64

# public key
with open("C:\\Users\\ryank\\OneDrive\\Desktop\\CleanUp\\School\\Year2\\Semester 2\\Capstone\\Operation RESL\\Test Files\\public.pem", "rb") as f:
#public_key = "C:\\Users\\ryank\\OneDrive\\Desktop\\CleanUp\\School\\Year2\\Semester 2\\Capstone\\Operation RESL\\Test Files\\public.pem"
    public_key = RSA.import_key(f.read())


# Encrypting?
data_to_encrypt = b"This needs to be encrypted"
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted = cipher_rsa.encrypt(data_to_encrypt)

encrypted_base64 = base64.b64encode(encrypted)

file_path = "C:\\Users\\ryank\\OneDrive\\Desktop\\CleanUp\\School\\Year2\\Semester 2\\Capstone\\Operation RESL\\Test Files\\encrypted_data.txt"
with open(file_path, "w") as encrypted_file:
    encrypted_file.write(encrypted_base64.decode())

print("Encrypted data")