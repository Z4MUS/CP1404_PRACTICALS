from SEM_2_PRACTICALS.prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
    another_guitar = Guitar("Another Guitar", 2013)
    age = gibson.get_age()
    print(f"{gibson.name} get_age() - Expected 99. Got {age}")
    age = another_guitar.get_age()
    print(f"{another_guitar.name} get_age() - Expected 8. Got {age}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    main()