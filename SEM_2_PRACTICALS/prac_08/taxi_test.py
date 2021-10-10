from SEM_2_PRACTICALS.prac_08.taxi import Taxi

Prius = Taxi(100, "Prius 1")
Prius.drive(40)
print(f"{Prius}, Current Fare: ${Prius.get_fare():,.2f}")
Prius.start_fare()
Prius.drive(100)
print(f"{Prius}, Current Fare: ${Prius.get_fare():,.2f}")