import random
import datetime

# Data for password generation
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
             'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

# take user inputs
passwordLength = int(input('Your password length: '))
includeDigits = bool(input("Must include numbers? (type True if you want to include else don't type anything.."))


# Function to generate a random password
def generate_password(length):
    if includeDigits:
        # Combine all characters
        all_characters = alphabets + digits + symbols
        password = ''.join(random.choice(all_characters) for _ in range(length))
        return password
    else:
        all_characters = alphabets + symbols
        password = ''.join(random.choice(all_characters) for _ in range(length))
        return password


print(f'Your Password 🔐: {generate_password(passwordLength)}')


