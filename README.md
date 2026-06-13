# Password Strength Checker

A simple command-line tool that checks how strong a password is.

## What it does

- Asks the user to enter a password
- Checks the length (8+ characters recommended)
- Checks for digits, uppercase letters, lowercase letters, and special characters
- Gives an overall rating: Strong, Medium, or Weak

## How to run
```
python password_checker.py
```

## What I learned

- String methods: `.isdigit()`, `.isupper()`, `.islower()`, `.isalnum()`
- Looping through characters in a string
- Combining conditions with `and`/`or`, and the importance of parentheses for operator precedence
- Using booleans as numbers (`True` + `True` = 2) to build a simple scoring system
- Debugging real errors: IndentationError, logic bugs
