password = input("Enter a password to check:")
length = len(password)
print(f"Your password is {length} characters long.")
if length >= 8:
    print("Length: OK (8+ characters)")
else:
    print("Length: Too short (needs 8+ characters)")
has_digit = False
has_upper = False
has_special = False
has_lower = False
for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True
    if not char.isalnum():
        has_special = True
    if char.islower():
        has_lower = True

print(f"Has digit: {has_digit}")
print(f"Has uppercase: {has_upper}")
print(f"Has special: {has_special}")
print(f"Has lowercase: {has_lower}")
score = has_digit + has_upper + has_lower + has_special
print(f"Score: {score}")
if length >= 8 and score == 4:
    print("password is strong")
elif length >= 8 and (score == 2 or score == 3):
    print("password is medium")
else:
    print("password is weak")
