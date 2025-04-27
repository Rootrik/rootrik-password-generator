# 🔒 Rootrik Password Generator

A professional-grade, customizable password generator designed for simplicity, security, and ease of use.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python) 
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Key Features

- **Customizable Length:** Define your password length effortlessly.
- **Flexible Complexity:** Optionally include numbers and special characters.
- **Multiple Passwords:** Generate one or multiple passwords at once.
- **Automatic Saving:** Generated passwords are saved automatically to a `.txt` file.
- **Enhanced Terminal UI:** Clear and visually appealing output with Colorama styling.
- **Robust Error Handling:** Ensures smooth user experience without interruptions.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Rootrik/rootrik-password-generator.git
cd rootrik-password-generator
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage

Run the script:

```bash
python password_generator.py
```

You will be prompted to:

- Enter the desired password length.
- Choose whether to include numbers.
- Choose whether to include special characters.
- Specify how many passwords to generate.

Passwords will be displayed and automatically saved into `generated_passwords.txt`.

---

## 📦 Example Output

```plaintext
=== Rootrik Password Generator ===

Enter desired password length (default 12): 16
Include numbers? (y/n) [default: y]: y
Include special characters? (y/n) [default: y]: y
How many passwords to generate? (default 1): 3

Generated Password(s):
 - @s8G1hF#zvB!9rP2
 - x!A7pVt2$k0Lm*Qz
 - 4gW&n%R#Fv2tKb!h

Passwords saved to /path/to/your/project/generated_passwords.txt
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Credits

Developed with ❤️ by [Rootrik](https://github.com/Rootrik)
