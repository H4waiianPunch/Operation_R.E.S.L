# Modules to import
import sys
import json
import time
import CreateKeys
import TestFunction

#Save public keys
def save_public_keys(public_keys):
    with open('public.keys.json', 'w') as file:
        json.dump(public_keys, file)

#Load public keys
def load_public_keys():
    with open('public.keys.json', 'r') as file:
        data = json.load(file)
    return data

# Old check for if user is admin(all users are right now)
#def check_user(userID, pubkey):
#    public_keys = load_public_keys()
#    for user_dict in public_keys:
#        if user_dict.get('UserID') == userID and str(user_dict.get('Pubkey')) == str(pubkey):
#            return True
#    return False

def print_ascii_art(art):
    for line in art.splitlines():
        print(line)


ascii_art = """
$$$$$$\                                             $$\     $$\                           $$$$$$$\      $$$$$$$$\      $$$$$$\      $$\           
$$  __$$\                                           $$ |    \__|                          $$  __$$\     $$  _____|    $$  __$$\     $$ |          
$$ /  $$ | $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\   $$\  $$$$$$\  $$$$$$$\        $$ |  $$ |    $$ |          $$ /  \__|    $$ |          
$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\  \____$$\ \_$$  _|  $$ |$$  __$$\ $$  __$$\       $$$$$$$  |    $$$$$\        \$$$$$$\      $$ |          
$$ |  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__| $$$$$$$ |  $$ |    $$ |$$ /  $$ |$$ |  $$ |      $$  __$$<     $$  __|        \____$$\     $$ |          
$$ |  $$ |$$ |  $$ |$$   ____|$$ |      $$  __$$ |  $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |    $$ |          $$\   $$ |    $$ |          
 $$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |      \$$$$$$$ |  \$$$$  |$$ |\$$$$$$  |$$ |  $$ |      $$ |  $$ |$$\ $$$$$$$$\ $$\ \$$$$$$  |$$\ $$$$$$$$\ $$\ 
 \______/ $$  ____/  \_______|\__|       \_______|   \____/ \__| \______/ \__|  \__|      \__|  \__|\__|\________|\__| \______/ \__|\________|\__|
          $$ |                                                                                                                                    
          $$ |                                                                                                                                    
          \__|                                                                                                                                    
"""

print_ascii_art(ascii_art)

def mainpart():
    #c = wmi.WMI()

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

#def enter_admin_mode():
#    print("\nAdministrative Mode:")
#    decrypted_string, user_name = TestFunction.Allow()
#    if decrypted_string:
#        print("User authenticated.")
 #       administrative_menu(decrypted_string, user_name)
#    else:
 #       print("Access denied.")

def enter_admin_mode():
    print("\nAdministrative Mode:")
    result = TestFunction.Allow()
    if result is not None:
        decrypted_string, user_name = result
        print("User authenticated.")
        administrative_menu(decrypted_string, user_name)
    else:
        print("Access denied.")


def administrative_menu(current_user, user_name):
    while True:
        print("\nAdministrative Menu:")
        print("1. Create key pair")
        print("2. Delete key pair")
        print("3. List all key pairs")
        print("4. Exit to main menu")


        option = input("Enter your choice: ").strip()

        if option == '1':
            create_key_pair()
        elif option == '2':
            delete_key_pair(current_user, user_name)
        elif option == '3':
            list_key_pairs()
        elif option == '4':
            print("Exiting to main menu...")
            break
        else:
            print("Invalid option. Please enter a valid option (1, 2, or 3).")


def create_key_pair():
    print("You've selected to create a key pair.")
    time.sleep(1)
    print("Generating key pairs")
    CreateKeys.new_key_generation()
    add_public_key()

def add_public_key():
    username = input("Enter the name of the user: ")
    with open("C:\\Users\\ryank\\OneDrive\\Desktop\\CleanUp\\School\\Year2\\Semester 2\\Capstone\\Operation RESL\\Test Files\\testkeys\\public.pem", "rb") as public_file:
        public_key = public_file.read()
    public_key_str = public_key.decode()
    public_keys = load_public_keys()
    public_keys.append({"UserID": username, "Pubkey": public_key_str})
    save_public_keys(public_keys)

def list_key_pairs():
    with open("public.keys.json", "r") as file:
        userid = json.load(file)
    for d in userid:
        print(f"UserID: {d['UserID']} // HIDDEN PUB KEY") # Don't NEED to show the whole pubkey. To show the full key, put this in {d['Pubkey']}"

def delete_key_pair(current_user, user_name):
    print(user_name)
    print("You've selected to delete a key pair. Type 'quit' to exit")
    # Add your delete key pair functionality here
    while True:
        list_key_pairs()
        user_to_delete = input("Enter the UserID you want to delete: ").strip()

        if user_to_delete == 'quit':
            print("Exiting delete key pair mode...")
            break
        elif user_to_delete == user_name:
            print("You cannot delete your own Public Key.")
            break
        elif not any(user['UserID'] == user_to_delete for user in load_public_keys()):
            print("Error: User ID not found. Please enter a valid UserID.")
        else:
            public_keys = load_public_keys()
            updated_public_keys = [user for user in public_keys if user['UserID'] != user_to_delete]
            save_public_keys(updated_public_keys)
            print(f"Public key for '{user_to_delete}' has been deleted")
            break


def unlock_menu():
    print("You've selected the Unlock menu.")
    decrypted_string = TestFunction.Allow()

    if decrypted_string:
        print("Door unlocked.")
        print("Program closes in 5 seconds")
        time.sleep(5)
        sys.exit() #exits the program
    else:
        print("Access denied.")


if __name__ == "__main__":
   mainpart()
