from SEM_2_PRACTICALS.prac_08.unreliable_car import UnreliableCar
new_car = UnreliableCar("New Car", 100, 90)
old_car = UnreliableCar("Old Car", 100, 1)
old_car.drive(60)
print(f"{old_car}")
new_car.drive(60)
print(f"{new_car}")