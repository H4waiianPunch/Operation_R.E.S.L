import json
import sys

def format_key_for_json(user_id, key):
    formatted_key = {
        "UserID": user_id,
        "Pubkey": key.replace("\n", "\n")
    }
    return formatted_key

def append_key_to_json_file(user_id, key):
    formatted_key = format_key_for_json(user_id, key)
    try:
        with open('public.keys.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    data.append(formatted_key)

    with open('public.keys.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    user_id = input("Enter your name: ").strip()

    print("Enter public key (press Ctrl+D when finished):")
    key = sys.stdin.read().strip()

    append_key_to_json_file(user_id, key)

    print("Key formatted and appended to public.keys.json")

if __name__ == "__main__":
    main()
