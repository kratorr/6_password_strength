
# Password Strength Calculator
This program prints to the console password strength after input

# How to Install

Python 3 should be already installed.

# Quickstart

The program must be run using the console, the required argument is the file with blacklist passwords.

How to run:
```bash
$ python3 password_strength.py <file_path>
```
Example of blacklist passwords:
```bash
$ cat passwords.txt
1234567
password
hello
```
Example of script launch on Linux, Python 3.5:
```bash
$ python3 password_strength.py passwords.txt
Input password: superpass
Your password strength (1-10):  4
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
