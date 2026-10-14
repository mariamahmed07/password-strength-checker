# 🔐 Password Strength Checker

A Python-based command-line application that evaluates password strength using basic security rules and provides suggestions to help users create stronger passwords.

Built as part of my **30 Projects in 30 Days** challenge to practice Python programming and explore cybersecurity concepts.

## ✨ Features

- **Password Length Analysis:** Checks password length and rewards longer passwords.
- **Character Validation:** Detects uppercase letters, lowercase letters, numbers, and special characters.
- **Common Password Detection:** Flags passwords found in a small list of commonly used passwords.
- **Predictable Pattern Detection:** Identifies selected sequences and keyboard patterns.
- **Strength Classification:** Categorizes passwords as Very Weak, Weak, Moderate, Strong, or Very Strong.
- **Improvement Suggestions:** Provides feedback based on the checks a password fails.
- **Automated Testing:** Includes basic test cases to verify expected classifications.

## 🛠️ Technologies Used

- Python 3
- Functions
- Conditional Statements
- Loops
- Strings and Sets
- List Comprehensions
- Exception-Free Input Validation
- Basic Automated Testing

## 🚀 Getting Started

### Prerequisites

- Python 3 installed on your computer, or access to an online Python compiler such as Programiz.

### Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/password-strength-checker.git
   ```

2. Open the project directory:

   ```bash
   cd password-strength-checker
   ```

3. Run the application:

   ```bash
   python main.py
   ```

Replace `YOUR-USERNAME` with your GitHub username.

## 🧪 Running the Tests

To run the automated tests, temporarily change the final lines in `main.py` to:

```python
if __name__ == "__main__":
    run_tests()
```

Then execute:

```bash
python main.py
```

The current test suite includes five cases covering empty input, common passwords, numeric passwords, a password that meets all configured checks, and a short password.

**Test result:** 5/5 tests passed in the tested environment.

Restore the final lines to `main()` to run the interactive application normally.

## 📋 Example

```text
========================================
      PASSWORD STRENGTH CHECKER
========================================

--- Password Analysis ---
Estimated strength: Very Strong
Rule score: 6/6

Educational tool only; not a security guarantee.
Never enter a real account password.
```

The example illustrates the output format. Actual results depend on the password entered.

## 🔒 Security Disclaimer

This is an educational project, not a professional password auditing tool.

- The common-password list is limited and is not comprehensive.
- The scoring system is rule-based and does not measure actual resistance to attacks.
- A high score does not guarantee that a password is secure.
- Do not enter real account passwords into this demonstration application.

## 🔮 Future Improvements

- Expand common-password and predictable-pattern detection.
- Improve password strength estimation.
- Add automated unit tests using Python's `unittest` framework.
- Create a graphical user interface.
- Add more comprehensive test coverage.

## 🎯 Learning Objectives

This project helped me practice:

- Writing reusable Python functions.
- Processing and validating strings.
- Working with sets and lists.
- Applying conditional logic.
- Designing basic automated tests.
- Exploring introductory cybersecurity concepts.

## 👩‍💻 Author

**Mariam Ahmed**

Computer Science and Artificial Intelligence Student

GitHub: [mariamahmed07](https://github.com/mariamahmed07)

---

*Part of my 30 Projects in 30 Days challenge.*
