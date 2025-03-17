# 🔒 Strong Password Generator

## 📜 Description

This Python script generates **strong and secure passwords** based on user input. It ensures security by including a mix of:
✅ Uppercase letters (A-Z)
✅ Lowercase letters (a-z)
✅ Digits (0-9)
✅ Special characters (`#$&!@%`)

Users can:

- Specify the **password length** (minimum 6 characters).
- **Optionally add a prefix** to the password.
- Ensure at least one character from each category is included.
- Get a **randomly shuffled password** for better security.

## ✨ Features

- 🔢 **User-defined password length** (minimum 6 characters).
- 🔡 **Optional prefix support** (ensures enough space for secure characters).
- 🔀 **Randomized password generation** for better security.
- 🔒 **Uses only secure characters** (no ambiguous symbols).

## 📌 Prerequisites

📌 **Python 3.x** must be installed on your system.

## 🛠 Installation

No additional libraries are required! The script only uses built-in Python modules (`random` and `string`).

## ▶️ How to Run

1️⃣ **Download the script** or copy the `strong_password_generator.py` file.
2️⃣ **Run the script** using Python:

```sh
python strong_password_generator.py
```

3️⃣ **Follow the prompts**:

- Enter the desired **password length** (minimum 6).
- Choose whether to **add a prefix**.
- If a prefix is chosen, enter it (prefix length should not exceed `password length - 6`).
  4️⃣ The **generated strong password** will be displayed.

---

## 📝 Example Usage

### ✅ Example 1: Generating a password **without a prefix**

```
Enter the desired password length (minimum 6): 12
Do you want a prefix? (yes/no, y/n): n
Generated Strong Password: @Tg4&yPb1!L
```

### ✅ Example 2: Generating a password **with a prefix**

```
Enter the desired password length (minimum 6): 14
Do you want a prefix? (yes/no, y/n): y
Enter the prefix: Secure_
Generated Strong Password: Secure_@P1&!yB
```

### ❌ Example 3: **Entering an invalid password length**

```
Enter the desired password length (minimum 6): 5
Password length must be at least 6.
Enter the desired password length (minimum 6): 10
```

### ❌ Example 4: **Entering an invalid prefix length**

```
Enter the desired password length (minimum 6): 10
Do you want a prefix? (yes/no, y/n): y
Enter the prefix: TooLongPrefix
Prefix length should be at most 4 characters.
Enter the prefix: Yes_
Generated Strong Password: Yes_4P!yT@B
```

---

## ℹ️ Notes

🔹 The script ensures a minimum of **6 random characters** after the prefix to maintain password strength.
🔹 Special characters are **limited to**: `#$&!@%`.
🔹 The password is **shuffled** to improve randomness and security.

## 🏆 Why Use This Password Generator?

✅ **Ensures strong security** with at least 6 randomized characters.
✅ **Easy to use** with clear prompts.
✅ **No third-party dependencies** required.
✅ **Completely free and open-source**.

## 📄 License

📝 This project is licensed under the **MIT License**.

## 👨‍💻 Author



Developed by **Jay Chauhan** 🚀

🌐 Website: [www.dj-jay.in](http://www.dj-jay.in)
✉️ Email: contact@dj-jay.in
📞 Phone: 9313190741
