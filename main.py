# ============================================
# Password Strength Checker
# ============================================
COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
    "iloveyou",
}

SEQUENCES = {
    "12345678",
    "123456789",
    "abcdefgh",
    "qwertyui",
}


def check_password(password):
    suggestions = []

    if not password:
        return "Invalid", 0, ["Password cannot be empty."]

    normalized = password.lower()

    is_common = normalized in COMMON_PASSWORDS
    is_sequence = normalized in SEQUENCES

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    score = 0

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check character variety
    if has_upper:
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if has_lower:
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if has_digit:
        score += 1
    else:
        suggestions.append("Add a number.")

    if has_symbol:
        score += 1
    else:
        suggestions.append("Consider adding a special character.")

    # Check predictable passwords
    if is_common:
        suggestions.append("Avoid common passwords.")

    if is_sequence:
        suggestions.append(
            "Avoid predictable sequences and keyboard patterns."
        )

    # Estimate password strength
    if is_common or is_sequence or len(password) < 8:
        strength = "Very Weak"
    elif score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, score, suggestions


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter a test password: ")

    strength, score, suggestions = check_password(password)

    print("\n--- Password Analysis ---")
    print(f"Estimated strength: {strength}")
    print(f"Rule score: {score}/6")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("All basic checks passed!")

    print("\nEducational tool only; not a security guarantee.")
    print("Never enter a real account password.")


if __name__ == "__main__":
    main()
