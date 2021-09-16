class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${cost:.2f}"

    def get_age(self):
        return 2021 - self.year

    def is_vintage(self):
        return self.get_age() >= 50

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# The ‘old’ manual way to format text with string concatenation:
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# And with f-string formatting (introduced in Python 3.6)
print(f"My {name} was first made in {year} (that's right, {year}!)")

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}")

# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for number in numbers:
    print("Number is {:>5}".format(number))

# An f-string version of the above using the enumerate function, useful when you want the index and value
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:>5}")

print(f"{year} {name} for about ${int(cost)}!")

for i in range(0, 151, 50):
    print("{:4}".format(i))