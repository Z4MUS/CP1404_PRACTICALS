import random

number_of_picks = int(input("how many quick picks do you wish to generate: "))
for i in range(0,number_of_picks):
    numbers = []
    for j in range(0, 6):
        number = random.randint(1, 45)
        while number in numbers:
            number = random.randint(1, 45)
        numbers.append(number)
        numbers.sort()
    print(f"{numbers[0]:2} {numbers[1]:2} {numbers[2]:2} {numbers[3]:2} {numbers[4]:2} {numbers[5]:2}")
