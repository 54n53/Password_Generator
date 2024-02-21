# Password_Generator
Random and secure password generator in Python.

Use of the "secrets" module for the generation of random numbers used to generate the combination of characters that make up the password.
Reference: https://docs.python.org/3/library/secrets.html

The password must contain the character ";" because in case of a breach and the password is entered into a csv by the attacker, this character may be interpreted to determine a new box.

Another security point is that the password is never displayed on the screen, instead is copied directly to the clipboard.
