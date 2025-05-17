# Step 1: Define the dictionary of fruit prices
prices = {"Apple": 1000, "Banana": 500, "Mango": 1200}

# Step 2: Display each fruit and its price
print("Fruit Prices per kg:")
for fruit, price in prices.items():
    print(f"{fruit}: {price} RWF per kg")

# Step 3: Calculate and display the total cost for 2 kg of each fruit
total_cost = sum(price * 2 for price in prices.values())
print(f"\nTotal cost for 2 kg of each fruit: {total_cost} RWF")
