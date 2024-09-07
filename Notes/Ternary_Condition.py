"""
conditional expression = A one-line shortcut for the i-else statement
(ternary operator)

X if condition else Y
"""

# num = 6
# a = 2
# b = 4
age = 24
user_role = "Admin"

# print("Positive" if num > 2 else "Negative")
# result = "Even" if num % 2 == 0 else "Odd"
# max_num = a if a > b else b

status = "Adult" if age >= 18 else "Child"
access_level = "Full Access" if user_role == "Admin" else "Limited Access"


print(access_level)
