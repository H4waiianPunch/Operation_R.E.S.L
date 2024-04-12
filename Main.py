import wmi
import sys
#from Crypto.PublicKey import RSA
#from PublicKeyDictionary import PublicKeyUser
import json
#import os
import time

import TestFunction


#charles work below
def save_public_keys(public_keys):
    # Convert keys and values to strings before saving
    public_keys_str = {str(k): str(v) for k, v in public_keys.items()}
    with open('public.keys.json', 'w') as file:
        json.dump(public_keys_str, file)


#charles work below
def load_public_keys():
    with open('public.keys.json', 'r') as file:
        data = json.load(file)
    return data

def check_user(userID, pubkey):
    public_keys = load_public_keys()
    for user_dict in public_keys:
        if user_dict.get('UserID') == userID and str(user_dict.get('Pubkey')) == str(pubkey):
            return True
    return False


def print_ascii_art(art):
    for line in art.splitlines():
        print(line)


ascii_art = """
   ____        _____       ____        _     
  |  _ \\      | ____|       / ___|     | |    
  | |_) |      |  _|        \\___ \\    | |    
  |  _ <   _   | |___   _   ___) |  _   | |___ 
  |_|\\_\\(_)  |_____| (_)  |____/ (_)  |_____|
"""

print_ascii_art(ascii_art)



def detect_usb():
    c = wmi.WMI()

    while True:
        print("\nSelect an option:")
        print("1. Administrative")
        print("2. Unlock")
        print("3. Exit")

        option = input("Enter your choice: ").strip()

        if option == '1':
            enter_admin_mode()
        elif option == '2':
            unlock_menu()
        elif option == '3':
            print("Exiting program...")
            sys.exit(0)
        else:
            print("Invalid option. Please enter a valid option (1, 2, or 3).")

#Charles work below

def enter_admin_mode():
    print("\nAdministrative Mode:")
    userID = input("Enter your name: ").strip()
    #pubkey = input("Enter your public key: ").strip()
    pubkey = TestFunction.load_private_key()

    if check_user(userID, pubkey):
        administrative_menu()
    else:
        print(f"Access denied. User ID: '{userID}', Public key: '{pubkey}'")


def administrative_menu():
    while True:
        print("\nAdministrative Menu:")
        print("1. Create key pair")
        print("2. Delete key pair")
        print("3. Exit to main menu")

        option = input("Enter your choice: ").strip()

        if option == '1':
            create_key_pair()
        elif option == '2':
            delete_key_pair()
        elif option == '3':
            print("Exiting to main menu...")
            break
        else:
            print("Invalid option. Please enter a valid option (1, 2, or 3).")


def create_key_pair():
    print("You've selected to create a key pair.")
    add_public_key()

def add_public_key():
    username = input("Enter the name of the user: ")
    public_key = input("Enter the public key for {}: ".format(username))

    public_keys = load_public_keys()
    public_keys[username] = public_key
    save_public_keys(public_keys)

def delete_key_pair():
    print("You've selected to delete a key pair.")
    # Add your delete key pair functionality here


def unlock_menu():
    print("You've selected the Unlock menu.")
    # Add your unlock menu functionality here


if __name__ == "__main__":
    detect_usb()
