import random
import string

def generate_password(length, options):
    password = ''
    if 'uppercase' in options:
        password += random.choice(string.ascii_uppercase)
    if 'lowercase' in options:
        password += random.choice(string.ascii_lowercase)
    if 'digits' in options:
        password += random.choice(string.digits)
    if 'special' in options:
        password += random.choice(string.punctuation)

    remaining_length = length - len(password)
    characters = ''
    if 'uppercase' in options:
        characters += string.ascii_uppercase
    if 'lowercase' in options:
        characters += string.ascii_lowercase
    if 'digits' in options:
        characters += string.digits
    if 'special' in options:
        characters += string.punctuation

    password += ''.join(random.choice(characters) for _ in range(remaining_length))
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    options = []

    print("Select your password specifications:")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Digits")
    print("4. Special characters")
    print("Enter 0 when finished selecting.")

    while True:
        choice = input("Enter your choice (1-4) or 0 to finish: ")
        if choice == '0':
            break
        elif choice == '1':
            options.append('uppercase')
        elif choice == '2':
            options.append('lowercase')
        elif choice == '3':
            options.append('digits')
        elif choice == '4':
            options.append('special')
        else:
            print("Invalid choice. Please enter a number from 1 to 4 or 0 to finish.")

    if not options:
        print("You must select at least one option.")
        return

    password = generate_password(length, options)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
