import cryptography
import os, json, getpass
from cryptography.fernet import Fernet
import string, random
import argparse

def generate_key():
    if not os.path.exists(".secret.key"):
        key = Fernet.generate_key()
        print(key.decode())
        with open(".secret.key", "wb") as key_file:
            key_file.write(key)
     

m_master_password = "12345"

def load_key():
    return open(".secret.key", "rb").read()

def encrypt_key(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_key(password):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(password.encode()).decode()

def load_file():
    if not os.path.exists("password.json"):
        return{}
    with open("password.json", "r") as file:
        return json.load(file)
    
def save_file(data):
    with open("password.json", "w") as file:
        json.dump(data, file, indent=4)

def authenticate():
    master_password = input("Enter the master password: ")
    e_key = input("Enter the encryption key: ")
    if(master_password==m_master_password) and (e_key==load_key().decode()):
        return True
    else:
        return False
    
def add_pw():
    org = input("Enter the handles name: ")
    user = input("Enter the user id: ")
    pw = getpass.getpass("Enter password: ")

    encrypted_password = encrypt_key(pw)
    data = load_file()
    data[org] = {"username":user, "password": encrypted_password.decode()}
    save_file(data)
    print(f"The details for the {org} are added successfully!")

def view_details():
    data = load_file()
    if authenticate():
        for account, details in data.items():
            print(f"Account: {account}, Username: {details['username']}, Password: ********")
    else:
        print("Your authorization has failed!")

def reveal(acc_name):
    data = load_file()
    if authenticate():
        if acc_name in data:
            decrypted_password = decrypt_key(data[acc_name]['password'])
            print(f"Account: {acc_name}, Username: {data[acc_name]['username']}, Password: {decrypted_password}")
        else:
            print("Account not found in the database!")
    else:
        print("Your authorization has failed!")

def delete(acc_name):
    data = load_file()
    if authenticate():
        if acc_name in data:
            del data[acc_name]
            save_file(data)
            print(f"Account: {acc_name} deleted successfully!")
        else:
            print("Account not found in the database!")
    else:
        print("Your authorization has failed!")

def update(acc_name):
    data = load_file()
    if authenticate():
        if acc_name in data:
            password = getpass.getpass("Enter the new password: ")
            encrypted_password = encrypt_key(password)
            data[acc_name]['password'] = encrypted_password.decode()
            save_file(data)
            print(f"Password for Account: {acc_name} updated successfully!")
        else:
            print("Account not found in the database!")
    else:
        print("Your authorization has failed!")

def generate_password(length=12, complexity='medium'):
    if complexity == 'low':
        chars = string.ascii_letters
    elif complexity == 'medium':
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Terminal-based Password Manager")
    parser.add_argument("command", choices=["add", "view", "reveal", "delete", "update", "generate"], help="Command to execute")
    parser.add_argument("--account", help="Account name for reveal, delete, or update commands")
    parser.add_argument("--length", type=int, default=12, help="Length of the generated password")
    parser.add_argument("--complexity", choices=['low', 'medium', 'high'], default='medium', help="Complexity of the generated password")

    args = parser.parse_args()

    generate_key()

    if args.command == "add":
        add_pw()
    elif args.command == "view":
        view_details()
    elif args.command == "reveal":
        if args.account:
            reveal(args.account)
        else:
            print("Account name is required for reveal command.")
    elif args.command == "delete":
        if args.account:
            delete(args.account)
        else:
            print("Account name is required for delete command.")
    elif args.command == "update":
        if args.account:
            update(args.account)
        else:
            print("Account name is required for update command.")
    elif args.command == "generate":
        password = generate_password(length=args.length, complexity=args.complexity)
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
