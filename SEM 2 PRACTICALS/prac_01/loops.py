"""
CP1404/CP5632 - Practical
loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(1, 21, -1):
    print(i, end=' ')

stars = int(input("Number of stars: "))
stars_line = stars * "*"
print(stars_line)

stars = int(input("Number of stars: "))
for i in range(stars + 1):
    star_line = i * "*"
    print(star_line)


