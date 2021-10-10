from SEM_2_PRACTICALS.prac_06.guitar import Guitar

MIN_YEAR = 0
MIN_COST = 0


def main():
    guitars = []
    print("My guitars!")
    get_guitars(guitars)
    print("""
    ... snip ...
    """)
    display_guitars(guitars,)


def get_guitars(guitars):
    name = input("Name: ").title()
    while name != "":
        year = int(get_valid_number("Year: ", MIN_YEAR))
        cost = get_valid_number("Cost: $", MIN_COST)
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ")
    return guitars


def get_valid_number(prompt, minimum):
    number = float(input(prompt))
    while number < minimum:
        print("invalid number")
        number = input(prompt)
    return number


def display_guitars(guitars):
    print("These are my guitars")
    for guitar in guitars:
        if guitar.is_vintage():
            vintage_status = "(vintage)"
        else:
            vintage_status = ""
        index = guitars.index(guitar) + 1
        print(f"Guitar {index}: {guitar.name:21} ({guitar.year}), worth ${guitar.cost:6,.2f} {vintage_status}")


if __name__ == '__main__':
    main()
