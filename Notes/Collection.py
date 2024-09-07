"""
Collection = single 'variable' used to store multiple values

List = [] ordered and changeable , Duplicates ok
Set = {} unordered and immutable , but Add/Remove Ok. No Duplicates
Tuple = () ordered and unchangeable. Duplicates Ok. Faster
"""

# LIST.............................

fruits = ["apple", "orange", "banana", "coconut", "grippes"]

# print(fruits[0: 2])
# print(fruits[:: 2])
# print(fruits[::-1])

# Get methods that can be used on the list
# print(dir(fruits))
# print(help(fruits))

fruits.remove("coconut")
fruits.insert(1, "pineapple")
fruits.sort()
fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("apple"))
# print(fruits)


# SET...............................

set_fruits = {"apple", "orange", "banana", "coconut"}
# print(dir(set_fruits))
# print(help(set_fruits))
# print(len(set_fruits))


# print("apple" in set_fruits)
set_fruits.add("apple")
set_fruits.add("orange")
# print(set_fruits)  # No Duplicates

# set_fruits.remove("coconut")
# set_fruits.pop()
# print(set_fruits.difference({"apple", "orange", "banana"}), "Difference")

# print(set_fruits)


# TUPLES

tuples_fruits = ("apple", "orange", "banana", "coconut")

# print(dir(tuples_fruits))
# print(help(tuples_fruits))
# print(len(tuples_fruits))


print(tuples_fruits.index("apple"))
print(tuples_fruits.count("banana"))

for fruit in tuples_fruits:
    print(f"# - {fruit}")
