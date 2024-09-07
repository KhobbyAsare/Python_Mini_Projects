"""
Format Specifier = {value:flags} format a value based on what
                        flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# "^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator
"""

# Practices

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# decimal points '.2f' - 2 decimal points
print(f"price 1 is {price1:.2f}")
print(f"price 2 is {price2:.2f}")
print(f"price 3 is {price3:.2f}")


# allocate space for a value
print("...................")
print(f"price 1 is {price1:10}")
print(f"price 2 is {price2:10}")
print(f"price 3 is {price3:10}")

# allocate and zero pad that many spaces
print("...................")
print(f"price 1 is {price1:010}")
print(f"price 2 is {price2:010}")
print(f"price 3 is {price3:010}")


# left justify
print("...................")
print(f"price 1 is {price1:<010}")
print(f"price 2 is {price2:<010}")
print(f"price 3 is {price3:<010}")

# right justify
print("...................")
print(f"price 1 is {price1:>010}")
print(f"price 2 is {price2:>010}")
print(f"price 3 is {price3:>010}")

# center align
print("...................")
print(f"price 1 is {price1:^10}")
print(f"price 2 is {price2:^10}")
print(f"price 3 is {price3:^10}")

# use a plus sign to indicate positive value
print("...................")
print(f"price 1 is {price1:+}")
print(f"price 2 is {price2:+}")
print(f"price 3 is {price3:+}")
print("........ OR ...........")
print(f"price 1 is {price1: }")
print(f"price 2 is {price2: }")
print(f"price 3 is {price3: }")

# use a minus sign to indicate Negative value
print("...................")
print(f"price 1 is {price1:-}")
print(f"price 2 is {price2:-}")
print(f"price 3 is {price3:-}")

# comma separator
price4 = 30005.14159
price5 = -987454.65
price6 = 124545.34

print("...................")
print(f"price 1 is {price4:,}")
print(f"price 2 is {price5:,}")
print(f"price 3 is {price6:,}")
print("........OR...........2 DECIMAL POINTS FOR EACH DIGIT")
print(f"price 1 is ${price4:,.2f}")
print(f"price 2 is ${price5:,.2f}")
print(f"price 3 is ${price6:,.2f}")