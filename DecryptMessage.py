# Importing RSA
from Crypto.PublicKey import RSA

# Importing a cipher thing needed for encryption/decryption
from Crypto.Cipher import PKCS1_OAEP

# Base64 for displaying the encrypted data in a txt file?
import base64

with open("C:\\Users\\ryank\\OneDrive\\Desktop\\CleanUp\\School\\Year2\\Semester 2\\Capstone\\Operation RESL\\Test Files\\private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

file_path = ("C:\\Users\\ryank\\OneDrive\\Desktop\\CleanUp\\School\\Year2\\Semester 2\\Capstone\\Operation RESL\\Test Files\\encrypted_data.txt")
with open(file_path, "r") as encrypted_file:
    encrypted_base64 = encrypted_file.read()

encrypted = base64.b64decode(encrypted_base64)
cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = cipher_rsa.decrypt(encrypted)

# Write it to a file
decrypted_file_path = "C:\\Users\\ryank\\OneDrive\\Desktop\\CleanUp\\School\\Year2\\Semester 2\\Capstone\\Operation RESL\\Test Files\\decrypted_data.txt"
with open(decrypted_file_path, "w") as decrypted_file:
    decrypted_file.write(decrypted.decode())

print("Decrypted data:", decrypted.decode())