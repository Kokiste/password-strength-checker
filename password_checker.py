from zxcvbn import zxcvbn
def check_password(password):
    length = len(password)
    if length < 8:
        return "Weak — password is too short (needs 8+ characters)"
    
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

    score = int(has_digit) + int(has_upper) + int(has_lower) + int(has_special)

    zxcvbn_result = zxcvbn(password)
    zxcvbn_score = zxcvbn_result["score"]

    if score == 4 and zxcvbn_score >= 3:
        return "Strong"
    elif score in (2, 3) and zxcvbn_score >= 2:
        return "Medium"
    else:
        return "Weak"
    
password = input("Enter a password to check: ")
result = check_password(password)
print(result)
