from cryptography.fernet import Fernet
import os
from Menu import *

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
            break
        else:
            print("Invalid choice. Please try again.")


def read_from_file():
    with open("users.txt", "r") as file:
        return file.readlines()

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
            username, password, _, _ = user.strip().split(",")

            if self.usernameField == username and self.passwordField == password:
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

        Menu()


def write_to_file(data):
    with open("users.txt", "a") as file:
        file.write(data + "\n")

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
            username, _, _, _ = user.strip().split(",")
            if self.newUserNameField == username:
                print("Username already exists. Please choose a different username.")
                return

        # Save the information to a text file
        data = f"{self.newUserNameField},{self.newPasswordField},{self.firstNameField},{self.lastNameField}\n"
        write_to_file(data)

        print("Successfully registered!")

    def run(self):
        print("Welcome to the Sellify registration page!")
        self.firstNameField = input("Enter your first name: ")
        self.lastNameField = input("Enter your last name: ")
        self.newUserNameField = input("Enter your username: ")
        self.newPasswordField = input("Enter your password: ")
        self.confirmPasswordField = input("Confirm your password: ")
        self.register()

if __name__ == "__main__":
    if not os.path.isfile("users.txt"):
        open("users.txt", "w").close()
    LoginMenu()
