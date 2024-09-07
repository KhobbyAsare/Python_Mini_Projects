#  Python Compound Interest Calculator

principal = 0
rate = 0
time = 0

# while principal <= 0:
#     principal = float(input("Enter the principal amount: "))
#     if principal <= 0:
#         print("Principal can not be less than or equal to 0")

while True:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal can not be less than or equal to 0")
    else:
        break


# while rate <= 0:
#     rate = float(input("Enter the Interest Rate amount: "))
#     if rate <= 0:
#         print("Interest Rate can not be less than or equal to 0")

while True:
    rate = float(input("Enter the Interest Rate amount: "))
    if rate <= 0:
        print("Interest Rate can not be less than or equal to 0")
    else:
        break


# while time <= 0:
#     time = float(input("Enter the time amount: "))
#     if time <= 0:
#         print("Time can not be less than or equal to 0")

while True:
    time = float(input("Enter the time amount: "))
    if time <= 0:
        print("Time can not be less than or equal to 0")
    else:
        break


total = principal * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:,.2f}")