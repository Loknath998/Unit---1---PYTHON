print("--- Password Strength Analyzer ---")
password = input("Enter password to evaluate: ")

score = 0
has_upper = False
has_lower = False
has_digit = False
has_special = False

if len(password) >= 8:
    score += 1

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True

if has_upper: score += 1
if has_lower: score += 1
if has_digit: score += 1
if has_special: score += 1

print("\n--- Security Report ---")
print(f"Total Points: {score}/5")

if score == 5:
    print("Strength: VERY STRONG")
elif score >= 3:
    print("Strength: MEDIUM")
else:
    print("Strength: WEAK")
