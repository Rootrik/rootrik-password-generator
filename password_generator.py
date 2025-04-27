#!/usr/bin/env python3
"""
Rootrik Password Generator
A simple, customizable password generator tool with terminal UI enhancements.
"""

import random
import string
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def generate_password(length=12, use_numbers=True, use_specials=True):
    """
    Generate a random password based on given criteria.

    Args:
        length (int): Length of the password.
        use_numbers (bool): Include digits if True.
        use_specials (bool): Include special characters if True.

    Returns:
        str: Generated password.
    """
    characters = list(string.ascii_letters)

    if use_numbers:
        characters += list(string.digits)
    if use_specials:
        characters += list(string.punctuation)

    if not characters:
        raise ValueError("No characters available to generate password!")

    return ''.join(random.choice(characters) for _ in range(length))

def save_password(password, filename="generated_passwords.txt"):
    """
    Save the generated password to a text file.

    Args:
        password (str): Password to save.
        filename (str): File to save password into.
    """
    with open(filename, "a") as f:
        f.write(password + "\n")

def main():
    """
    Main function to handle user input and generate passwords.
    """
    print(Fore.CYAN + "=== Rootrik Password Generator ===\n")
    
    try:
        length = int(input(Fore.YELLOW + "Enter desired password length (default 12): ") or 12)
        numbers = input(Fore.YELLOW + "Include numbers? (y/n) [default: y]: ").lower() or 'y'
        specials = input(Fore.YELLOW + "Include special characters? (y/n) [default: y]: ").lower() or 'y'
        quantity = int(input(Fore.YELLOW + "How many passwords to generate? (default 1): ") or 1)

        use_numbers = numbers == 'y'
        use_specials = specials == 'y'

        passwords = [generate_password(length, use_numbers, use_specials) for _ in range(quantity)]

        print(Fore.GREEN + "\nGenerated Password(s):")
        for pwd in passwords:
            print(Fore.WHITE + f" - {pwd}")
            save_password(pwd)

        print(Fore.GREEN + f"\nPasswords saved to {os.path.abspath('generated_passwords.txt')}")

    except ValueError as ve:
        print(Fore.RED + f"Error: {ve}")
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
