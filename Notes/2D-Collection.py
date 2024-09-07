# List
fruits = ["Apple", "Banana", "Orange", "Strawberry", "Grapes"]
vegetables = ["Carrot", "Broccoli", "Spinach", "Pepper", "Cabbage"]
meats = ["Chicken", "Beef", "Pork", "Lamb", "Turkey"]

groceries = [fruits, vegetables, meats]

print(groceries)
print(groceries[2][0])

for collection in groceries:
    for item in collection:
        print(item, end=" ")

    print()

# Tuples

tuplesGroceries = [
    ("Mango", "Pineapple", "Kiwi", "Blueberry", "Papaya"),
    ("Tomato", "Cucumber", "Lettuce", "Zucchini", "Eggplant"),
    ("Duck", "Venison", "Salmon", "Goat", "Bacon")
]

print(tuplesGroceries)

setGroceries = [
    {"Mango", "Pineapple", "Kiwi", "Blueberry", "Papaya"},
    {"Tomato", "Cucumber", "Lettuce", "Zucchini", "Eggplant"},
    {"Duck", "Venison", "Salmon", "Goat", "Bacon"}
]

print(setGroceries)
