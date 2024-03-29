import secrets # https://docs.python.org/3/library/secrets.htmls
import pyperclip
<<<<<<< HEAD
import getpass
#import string
=======
import string
>>>>>>> refs/remotes/origin/main

def password_generator(length):
    #characters = string.ascii_letters + string.digits + string.punctuation # Added: "ñ", "Ñ", "ç" and "Ç".
    characters = "abcdefghijklmnñopqrstuvwxyzçABCDEFGHIJKLMNÑOPQRSTUVWXYZÇ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    while True:
        password = ''.join(secrets.choice(characters) for i in range(length))
        if ';' in password:
            return password

def main():
    while True:
        try:
            #length = int(input("Enter password length (must be longer than 12 characters): "))
            length = int(getpass.getpass("Enter password length (must be longer than 12 characters): "))
            if length >= 12:
                password = password_generator(length)
                pyperclip.copy(password)  # Copy the password to the clipboard
                print("The generated password has been copied to the clipboard.")
                break
            else:
                print("Password length must be longer than 12 characters. Please try again.")
        except ValueError:
            print("Please enter a valid length.")

if __name__ == "__main__":
    main()
