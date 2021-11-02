"""
CP1404/CP5632 - Practical
shop calculator 
"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
total = 0
for i in range(number_of_items + 1):
    price = float(input("Price of item: "))
    if price > 100:
        new_price = 0.9 * price
        total += new_price
    else:
        total += price
print(f"Total price for {number_of_items} items is: ${total}")