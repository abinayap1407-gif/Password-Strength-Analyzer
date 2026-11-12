print("==============================")
print("  PASSWORD STRENGTH ANALYZER")
print("==============================")

password = input("Enter a sample password: ")


length = len(password)


has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:

    if ch.isupper():
        has_upper = True

    elif ch.islower():
        has_lower = True

    elif ch.isdigit():
        has_digit = True

    else:
        has_special = True


print("\nPassword Analysis")

print("Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Number:", has_digit)
print("Special character:", has_special)



score = 0

if length >= 8:
    score += 1

if length >= 12:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

print("\nPassword Score:", score, "/ 6")

if score <= 2:
    print("Strength: WEAK")

elif score <= 4:
    print("Strength: MEDIUM")

else:
    print("Strength: STRONG")

   

if len(password) == len(set(password)):
    print("Uniqueness: No repeated characters")
else:
    print("Uniqueness: Repeated characters found")

    

print("\nSuggestions:")

if length < 8:
    print("- Use at least 8 characters")

if not has_upper:
    print("- Add an uppercase letter")

if not has_lower:
    print("- Add a lowercase letter")

if not has_digit:
    print("- Add a number")

if not has_special:
    print("- Add a special character")

if len(password) != len(set(password)):
    print("- Avoid repeated characters")

if length >= 8 and has_upper and has_lower and has_digit and has_special and len(password) == len(set(password)):
    print("- Your password meets all basic checks!")