# file encrypt decrypt program

from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("🔑 Key generated and saved as 'secret.key'.")

def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("❌ Key file not found. Generate it first.")
        return None

def encrypt_file(filename, key):
    try:
        f = Fernet(key)
        with open(filename, "rb") as file:
            original = file.read()
        encrypted = f.encrypt(original)
        with open(filename + ".enc", "wb") as enc_file:
            enc_file.write(encrypted)
        print(f"🔒 Encrypted file saved as: {filename}.enc")
    except FileNotFoundError:
        print("❌ File not found.")

def decrypt_file(enc_filename, key):
    try:
        f = Fernet(key)
        with open(enc_filename, "rb") as file:
            encrypted = file.read()
        decrypted = f.decrypt(encrypted)
        output_file = "decrypted_" + enc_filename.replace(".enc", "")
        with open(output_file, "wb") as dec_file:
            dec_file.write(decrypted)
        print(f"🔓 Decrypted file saved as: {output_file}")
    except Exception as e:
        print("❌ Decryption failed:", e)

def main():
    while True:
        print("\n🔐 FILE ENCRYPTION/DECRYPTION")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            key = load_key()
            if key:
                filename = input("Enter filename to encrypt: ")
                encrypt_file(filename, key)
        elif choice == "3":
            key = load_key()
            if key:
                filename = input("Enter encrypted filename (.enc): ")
                decrypt_file(filename, key)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
