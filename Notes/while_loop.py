# while loop = executes some code WHILE some condition is true

age = int(input("Enter your age: "))

while age < 0:
    print("Age cant't be negative")
    age = int(input("Enter your age: "))

print(f"your age is {age}")

# ............................................

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("Exit")


# .........................

number = float(input("Enter a number 1 - 10: "))

while number < 1 or number > 10:
    print(f"{number} is not valid")
    number = float(input("Enter a number 1 - 10: "))

print(f" Your number is {number:.2f}")

