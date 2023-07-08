from cryptography.fernet import Fernet
import os
from MenuFunction import *

def LoginMenu():
    while True:
        print("+=================================================+")
        print("|            1. Login                             |")
        print("|            2. Register                          |")
        print("|            3. Quit                              |")
        print("+=================================================+")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            login_instance = Login()
            login_instance.run()
        elif choice == "2":
            register_instance = Registration()
            register_instance.run()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice. Please try again.")

def read_from_file():
    if not os.path.isfile("users.txt"):
        return []
    with open("users.txt", "r") as file:
        return file.readlines()

def write_to_file(data):
    with open("users.txt", "a") as file:
        file.write(data + "\n")

def generate_key():
    return Fernet.generate_key()

class Login:
    def __init__(self):
        self.usernameField = ""
        self.passwordField = ""

    def login(self):
        # Check if any of the fields are empty
        if not self.usernameField or not self.passwordField:
            print("Please enter your username and password.")
            return

        # Read user information from the file
        users = read_from_file()
        for user in users:
            encrypted_data = user.strip().split(",")
            if len(encrypted_data) != 4:
                continue

            encrypted_username, encrypted_password, encrypted_firstname, encrypted_lastname = encrypted_data

            key = self.load_key()
            decrypted_username = self.decrypt_data(key, encrypted_username)
            decrypted_password = self.decrypt_data(key, encrypted_password)

            if self.usernameField == decrypted_username and self.passwordField == decrypted_password:
                print("Login successful!")
                return

        print("Invalid username or password.")

    def run(self):
        print("+=================================================+")
        print("Welcome to the Sellify login page!")
        print("+=================================================+")
        self.usernameField = input("Enter your username: ")
        self.passwordField = input("Enter your password: ")
        print("+=================================================+")
        self.login()

        Menu_selection()

    def load_key(self):
        if os.path.isfile("key.txt"):
            with open("key.txt", "rb") as file:
                key = file.read()
            return key

    def decrypt_data(self, key, encrypted_data):
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(encrypted_data.encode()).decode()
        return decrypted_data


class Registration:
    def __init__(self):
        self.newUserNameField = ""
        self.newPasswordField = ""
        self.confirmPasswordField = ""
        self.firstNameField = ""
        self.lastNameField = ""

    def register(self):
        if self.newPasswordField != self.confirmPasswordField:
            print("Passwords do not match.")
            return

        # Check if any of the fields are empty
        if not self.firstNameField or not self.lastNameField or not self.newUserNameField or not self.newPasswordField:
            print("Please enter all of the required information.")
            return

        # Check if the username already exists
        users = read_from_file()
        for user in users:
            encrypted_data = user.strip().split(",")
            if len(encrypted_data) != 4:
                continue

            encrypted_username, _, _, _ = encrypted_data
            key = self.load_key()
            decrypted_username = self.decrypt_data(key, encrypted_username)

            if self.newUserNameField == decrypted_username:
                print("Username already exists. Please choose a different username.")
                return

        # Generate a key for encryption
        key = generate_key()

        # Save the key to a file
        with open("key.txt", "wb") as file:
            file.write(key)

        # Encrypt user data
        encrypted_username = self.encrypt_data(key, self.newUserNameField)
        encrypted_password = self.encrypt_data(key, self.newPasswordField)
        encrypted_firstname = self.encrypt_data(key, self.firstNameField)
        encrypted_lastname = self.encrypt_data(key, self.lastNameField)

        # Save the encrypted information to the file
        encrypted_data = f"{encrypted_username},{encrypted_password},{encrypted_firstname},{encrypted_lastname}"
        write_to_file(encrypted_data)

        print("Successfully registered!")

    def run(self):
        print("Welcome to the Sellify registration page!")
        self.firstNameField = input("Enter your first name: ")
        self.lastNameField = input("Enter your last name: ")
        self.newUserNameField = input("Enter your username: ")
        self.newPasswordField = input("Enter your password: ")
        self.confirmPasswordField = input("Confirm your password: ")
        self.register()

    def load_key(self):
        if os.path.isfile("key.txt"):
            with open("key.txt", "rb") as file:
                key = file.read()
            return key

    def encrypt_data(self, key, data):
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(data.encode()).decode()
        return encrypted_data


if __name__ == "__main__":
    if not os.path.isfile("users.txt"):
        open("users.txt", "w").close()
    LoginMenu()
