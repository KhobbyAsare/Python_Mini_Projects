"""
nested loop = A loop within another loop(outer, inner)

        outer loop:
            inner loop:
                do something
"""

for x in range(3):
    for y in range(1, 11):
        # end="-" will print the x all on the same line
        # instead of different lines
        # you can use " ", "-", "/" for the separation of each one
        # print(y, end=" ")
        pass

    # print("\n New Interation")

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter your preferred symbol (eg: *, # ): ")

for x in range(rows):  # Loop over the number of rows
    for y in range(columns):  # Loop over the number of columns
        print(symbol, end="")  # Print the symbol without a newline after each one
    print()  # After each row is printed, add a newline to move to the next row


# Incremental Shap

rows = int(input("Enter the # of rows: "))
symbol = input("Enter your preferred symbol (eg: *, # ): ")

for x in range(1, rows + 1):  # Loop from 1 to the number of rows
    print(symbol * x)  # Print the symbol 'x' times for each row

