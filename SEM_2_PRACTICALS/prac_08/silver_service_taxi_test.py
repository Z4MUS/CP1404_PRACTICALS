from SEM_2_PRACTICALS.prac_08.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi('Hummer', 200, 4)
tesla = SilverServiceTaxi('Tesla', 100, 2)
hummer.drive(35)
tesla.drive(18)

print(f"{hummer.name}, for 35km trip Expect fair of $176.70, Current Fair: ${hummer.get_fare():.2f}")
print(hummer)
print(f"{tesla.name}, for 18km trip Expect fair of $48.78, Current Fair: ${tesla.get_fare():.2f}")
print(tesla)