# 1. basic list operations
numbers = []
for i in range(1, 6):
    number = int(input("enter a number: "))
    numbers.append(number)

print(f"the first number is {numbers[0]}")
print(f"the last number is {numbers[-1]}")
print(f"the smallest number is {min(numbers)}")
print(f"the largest number is {max(numbers)}")
average = sum(numbers)/5
print(f"the average of the numbers is {average}")

# 2. woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("username: ").lower()
while username not in usernames:
    print("Access denied")
    username = input("username: ").lower()
print("Access granted")


