import random
import string


def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length should be a positive integer.")
                continue
            uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
            digits = input("Include digits? (y/n): ").lower() == 'y'
            symbols = input("Include symbols? (y/n): ").lower() == 'y'

            password = generate_password(length, uppercase, lowercase, digits, symbols)
            if password:
                print(f"Generated Password: {password}")

            break  # Exit the loop after generating the password
        except ValueError:
            print("Invalid input. Please enter a valid length.")


if __name__ == "__main__":
    main()


