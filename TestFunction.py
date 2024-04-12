import secrets
import string
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey.RSA import RsaKey
import json
import wmi
import sys

import USBIN


def load_public_keys():
    with open('public.keys.json', 'r') as file:
        data = json.load(file)
    return data

def load_private_key():
    with open("D:\private.pem", 'rb') as file:
        private_key = file.read()
    return private_key

def gen_rand_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for i in range(length))

def encrypt_rand_string(user_name):
    public_keys = load_public_keys()
    user_public_key = None
    for user_dict in public_keys:
        if user_dict.get('UserID') == user_name:
            user_public_key = user_dict.get('Pubkey')
            break
    if not user_public_key:
        print("User {} not found or does not have a public key.".format(user_name))
        return None

    # Load the RSA Public key
    rsa_key = RSA.import_key(user_public_key)
    cipher = PKCS1_OAEP.new(rsa_key)

    # Generate the random string
    rand_string = gen_rand_string(16)
    print("Random String:", rand_string)

    # Encrypt the random string
    encrypted_data = cipher.encrypt(rand_string.encode())
    return encrypted_data, rsa_key

def decrypt_data(encrypted_data, rsa_key: RsaKey):
    private_key = load_private_key()
    rsa_private_key = RSA.import_key(private_key)
    if rsa_private_key.n != rsa_key.n or rsa_private_key.e != rsa_key.e:
        print("Private key does not match the public key.")
        return None
    cipher = PKCS1_OAEP.new(rsa_private_key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode()



def main():
    USBIN.detect_usb()
    user_name = input("Enter your name: ")
    encrypted_string, rsa_key = encrypt_rand_string(user_name)
    if encrypted_string:
        print("Encrypted string:", encrypted_string.hex())
        decrypted_string = decrypt_data(encrypted_string, rsa_key)
        if decrypted_string:
            print("Decrypted string:", decrypted_string)
        else:
            print("Decryption unsuccessful.")

if __name__ == "__main__":
    main()
