"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        calculate_bonus(sales)
        sales = float(input("Enter sales: $"))
    print("goodbye")

def calculate_bonus(sales):
    if sales < 1000:
        print("for sales under $1000, you get a 10% bonus")
        bonus = 0.1 * sales
    else:
        print("for sales $1000 or over, you get a 15% bonus")
        bonus = 0.15 * sales
    print(f"bonus is: {bonus}")

main()