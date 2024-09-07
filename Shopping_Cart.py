# shopping cart program
import datetime

foods = []
prices = []
total_price = 0

# Input loop to gather food and price
while True:
    food = input("Enter a food to buy (q to exit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price for {food}: $"))
        foods.append(food)
        prices.append(price)

print("\n----- YOUR CART -----")

# Iterate through foods and prices together using zip()
for food, price in zip(foods, prices):
    print(f"{food}  ---- ${price:.2f}")
    
print(f" {datetime.datetime.now().date()} - {datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}:{datetime.datetime.now().time().second}"  )

# Calculate and print the total price
total_price = sum(prices)
print(f"\nTotal Price: ${total_price:.2f}")

