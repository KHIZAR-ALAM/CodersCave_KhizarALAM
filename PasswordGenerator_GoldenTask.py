import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    #this portion define character sets based on user selection 
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # this check if the user has selected any one character tyype
    if not characters:
        return "Error: No character types selected."

    # this generate random password
    password = ''.join(random.choice(characters) for _ in range(length))

    # this confirms that the password meets the requirments set by user
    if use_uppercase and not any(c.isupper() for c in password):
        password = insert_random_character(password, string.ascii_uppercase)
    if use_digits and not any(c.isdigit() for c in password):
        password = insert_random_character(password, string.digits)
    if use_special and not any(c in string.punctuation for c in password):
        password = insert_random_character(password, string.punctuation)

    return password

def insert_random_character(password, characters):
    index = random.randint(0, len(password) - 1)
    random_char = random.choice(characters)
    return password[:index] + random_char + password[index:]

while True:
    #these are input options
    print("Password Generator Options:")
    print("Enter 'generate' to generate a password")
    print("Enter 'quit' to exit the program")

    user_input = input(": ").lower()
    #this portion take actions as per input
    if user_input == "quit":
        break
    elif user_input == "generate":
        length = int(input("Enter password length: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
        use_digits = input("Include digits? (yes/no): ").lower() == "yes"
        use_special = input("Include special characters? (yes/no): ").lower() == "yes"
    
        password = generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_digits=use_digits,
            use_special=use_special,
        )

        print("Generated Password:", password)
    else:
        print("Invalid input")