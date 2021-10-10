from SEM_2_PRACTICALS.prac_08.taxi import Taxi
from SEM_2_PRACTICALS.prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>> "

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4), SilverServiceTaxi("Tesla", 200, 4)]
    bill = 0
    current_taxi = None
    choice = input(MENU).lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            list_taxis(taxis)
            taxi_choice = int(input("Choose Taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid Taxi choice")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                current_taxi.drive(int(input("Drive how far? ")))
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill += trip_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        choice = input(MENU).lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    list_taxis(taxis)


def list_taxis(taxis):
    return [print(f"{i} - {taxi}") for i, taxi in enumerate(taxis)]


main()