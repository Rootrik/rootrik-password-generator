import random
import string
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def generate_password(length=12, use_digits=True, use_special=True):
    """
    Generate a random password based on given parameters.

    :param length: Length of the password
    :param use_digits: Include numbers
    :param use_special: Include special characters
    :return: Generated password as a string
    """
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character set selected.")

    return ''.join(random.choice(characters) for _ in range(length))

def ask_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").lower()
        if answer in ('y', 'n'):
            return answer == 'y'
        print(Fore.RED + "Please enter 'y' or 'n'.")

def main():
    print(Fore.CYAN + Style.BRIGHT + "=== Rootrik Password Generator ===")
    
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Invalid input. Using default length: 12")
        length = 12

    include_digits = ask_yes_no("Include numbers?")
    include_special = ask_yes_no("Include special characters?")

    password = generate_password(length, include_digits, include_special)

    print(Fore.GREEN + f"\n✅ Your new password: {password}")

    with open("generated_password.txt", "w") as file:
        file.write(password)
    print(Fore.YELLOW + "💾 Password saved to 'generated_password.txt'")

if __name__ == "__main__":
    main()
