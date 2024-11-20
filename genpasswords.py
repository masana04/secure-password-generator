import string
import random

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    secure_random = random.SystemRandom()
    password = ''.join(secure_random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired password length (positive integer): "))
            if length <= 0:
                print("Password length must be greater than zero. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

    use_letters = get_yes_no_input("Include letters? (y/n): ")
    use_numbers = get_yes_no_input("Include numbers? (y/n): ")
    use_symbols = get_yes_no_input("Include symbols? (y/n): ")

    if not (use_letters or use_numbers or use_symbols):
        print("At least one character type must be selected. Please try again.")
        return get_user_input()

    return length, use_letters, use_numbers, use_symbols

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def display_header():
    print("=" * 50)
    print("★ ☆ ★ ☆ ★   P A S S W O R D   G E N E R A T O R   ★ ☆ ★ ☆ ★".center(50))
    print("=" * 50)

def main():
    display_header()
    length, use_letters, use_numbers, use_symbols = get_user_input()
    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
