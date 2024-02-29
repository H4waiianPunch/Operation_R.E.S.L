from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Grab the private key for decryption
with open("C:\\Users\\ryank\OneDrive\Desktop\CleanUp\School\Year2\Semester 2\Capstone\Operation RESL\Test Files\private.pem") as f:
    private_key = RSA.import_key(f.read())

# Decrypt filepath
decrypt_file_path = ("C:\\Users\\ryank\OneDrive\Desktop\CleanUp\School\Year2\Semester 2\Capstone\Operation RESL\Test Files\EncryptFile.txt")
with open(decrypt_file_path, "rb") as file:
    data_to_decrypt = file.read()

#decrypt
cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = cipher_rsa.decrypt(data_to_decrypt)

decrypted = decrypted.decode('utf-8')
print(decrypted)
