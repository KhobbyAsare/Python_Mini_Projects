name = "Hanks2 Mikes"

# result = len(name)
# result = name.find("s")  # First occurrence of a character
# result1 = name.rfind("s")  # Last occurrence of a character


# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()  # return True / False if a string contains only digits
# result = name.isalpha()  # return True / False if a string contains only alphabetical letters
# if there is a space in the string it will be false
# it will be true if there is no space or digits in the string

# name1 = "Kelly "
# result = name1.isalpha()

# phone_number = "1-234-567-980"
# result = phone_number.count("-")  # counting the number of dashes in the number
#
# word = "Hello Word"
#
# # result = word.replace("H", 'h')
# result = word.replace("W", 'K')

# print(result)

help(str)

# VALIDATION
"""
1. username is no more than 12 characters
2. username must not contain spaces
3. username must not contain digits

"""

username = input("Enter your Username: ")

if len(username) > 12:
    print("your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username must not contain spaces")
elif not username.isalpha():
    print("Your username can not contain numbers")
else:
    print(f"Welcome {username}")
