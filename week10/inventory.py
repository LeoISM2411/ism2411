# Lab 10
# 1. I think the most surprising thing about how lists work in Python compared to what I 
# expected coming in is that it's not fixed. You can easily add, remove and sort items without having to create an 
# an entirely new list.
# 2. One business situation where a Python list would have saved me time rather than doing it manually in excel
# is if I am trying to keep track of a company'sinventory. For example if it's a shoe company 
# I could use the python list to organize the different shoes they sell as well as calculate the average sales 
# to see which products are selling the most.
print("---Exercise 1: Build the List---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("---Exercise 2: Index Practice---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2
print(inventory[middle]) # middle item

print("---Exercise 3: Slicing---")
print(inventory[:3]) # first 3 items
print(inventory[-2:]) # last 2 items
print(inventory[::2])

print("--- Exercise 4: Modyfying the list ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try: 
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident")

print(coords)

print("--- Exercise 6: Average list of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7 ---")

prices = [9.99, 14.99, 4.99, 24.99 , 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * .9, 2))

print("Original prices:", prices)
print("Discounts:", discounted)

print("--- Exercise 8: Filter above a threshold")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High Sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")



