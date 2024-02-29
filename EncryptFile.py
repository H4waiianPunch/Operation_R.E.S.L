from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Grabbing the public key from public.pem
with open("C:\\Users\\ryank\OneDrive\Desktop\CleanUp\School\Year2\Semester 2\Capstone\Operation RESL\Test Files\public.pem") as f:
    public_key = RSA.import_key(f.read())

# Setting the filepath for the file I want to encrypt. This would be done differently in the end I imagine.
# We wouldn't want it to be a fixed path.
encrypt_file_path = ("C:\\Users\\ryank\OneDrive\Desktop\CleanUp\School\Year2\Semester 2\Capstone\Operation RESL\Test Files\EncryptFile.txt")
with open(encrypt_file_path, "rb") as file:
    data_to_encrypt = file.read()

#encrypting
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted = cipher_rsa.encrypt(data_to_encrypt)

#Write it to a path
encrypted_file_path = "C:\\Users\\ryank\\OneDrive\\Desktop\\CleanUp\\School\\Year2\\Semester 2\\Capstone\\Operation RESL\\Test Files\\encrypted_file.enc"
with open(encrypt_file_path, "wb") as encrypted_file:
    encrypted_file.write(encrypted)


