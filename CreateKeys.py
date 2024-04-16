# Creates private/public keys

from Crypto.PublicKey import RSA

def new_key_generation():
    # Generates private/public keys
    key = RSA.generate(2048)

    # Specifies the folder they're saved in. This would need to be a more generic location. Picked a specific one for testing
    save_dir = "C:\\Temp\\"

    # Extract private and public keys
    private_key = key.export_key()
    public_key = key.public_key().export_key()

    # Save the keys to the file specified
    with open(save_dir + "private.pem", "wb") as private_file:
        private_file.write(private_key)

    with open(save_dir + "public.pem", "wb") as public_file:
        public_file.write(public_key)

    print("Keys saved here", save_dir)

