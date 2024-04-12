import secrets
import string
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import json

def load_public_keys():
    with open('public.keys.json', 'r') as file:
        data = json.load(file)
    return data

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
    return encrypted_data

def main():
    user_name = input("Enter your name: ")
    encrypted_string = encrypt_rand_string(user_name)
    if encrypted_string:
        print("Encrypted string:", encrypted_string.hex())

if __name__ == "__main__":
    main()
