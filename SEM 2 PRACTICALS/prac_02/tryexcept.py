try:
    number = int(input("? "))
    print(10/number)
except ValueError:
    print("Not a valid integer")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Some other exception occurred")
print("Finished")



#prime example
valid_age = False
while not valid_age:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Invalid age - must be non-negative")
        else:
            valid_age = True
    except ValueError:
        print("Invalid age - enter a number")
print(f"You are {age} years old")