# PasswordManager
CLI based password manager using json and python to encrypt and decrypt passwords

# Terminal-Based Password Manager

## Overview
This is a lightweight, terminal-based password manager written in Python. The program encrypts your passwords for secure storage and allows you to easily retrieve, add, and manage your passwords directly from the command line.

## Features
- **Encryption**: Passwords are securely encrypted using standard encryption algorithms.
- **Command-line Interface**: Manage your passwords from the terminal with simple commands.
- **Secure Storage**: Passwords are stored in an encrypted format, ensuring that only you can access them.
- **Add, Retrieve, and Delete**: Easily add new credentials, retrieve existing ones, and delete old ones.
- **Master Password**: Protects all stored passwords using a master password.

Here’s the text you can add to your README file to explain how the command works:

---

## Usage

To run the password manager, navigate to the directory where your script is located and use the following command:

```bash
python password_manager.py <command> [--options]
```

### Commands

- **add**: Add a new account's password.
  
  ```bash
  python password_manager.py add
  ```

- **view**: View all stored account details (usernames and masked passwords).

  ```bash
  python password_manager.py view
  ```

- **reveal**: Reveal the password of a specific account.

  ```bash
  python password_manager.py reveal --account <account_name>
  ```

- **delete**: Delete a specific account's details.

  ```bash
  python password_manager.py delete --account <account_name>
  ```

- **update**: Update the password for a specific account.

  ```bash
  python password_manager.py update --account <account_name>
  ```

- **generate**: Generate a new password.

  ```bash
  python password_manager.py generate --length <password_length> --complexity <low|medium|high>
  ```

### Options

- `--account <account_name>`: Specify the account name for the `reveal`, `delete`, and `update` commands.
- `--length <password_length>`: Specify the length of the password for the `generate` command.
- `--complexity <low|medium|high>`: Specify the complexity of the password for the `generate` command. 
  - **low**: Only letters.
  - **medium**: Letters and numbers.
  - **high**: Letters, numbers, and special characters.

---

This text provides a concise explanation of how to use each command in your terminal-based password manager.
  
