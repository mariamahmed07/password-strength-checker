
from main import check_password


def run_tests():
    test_cases = [
        ("", "Invalid"),
        ("password", "Very Weak"),
        ("12345678", "Very Weak"),
        ("Ab1!", "Very Weak"),
        ("Blue!River82X", "Very Strong"),
    ]

    passed = 0
    total = len(test_cases)

    print("=" * 40)
    print("       AUTOMATED TESTS")
    print("=" * 40)

    for password, expected in test_cases:
        result, score, suggestions = check_password(password)

        if result == expected:
            print(f"PASS: {password!r} -> {result}")
            passed += 1
        else:
            print(
                f"FAIL: {password!r} -> {result}; "
                f"expected {expected}"
            )

    print(f"\nResult: {passed}/{total} tests passed.")


if __name__ == "__main__":
    run_tests()
