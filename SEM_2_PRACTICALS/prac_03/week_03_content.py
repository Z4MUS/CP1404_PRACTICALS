def main():
    age = 0
    valid_input = False
    while not valid_input:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be >=0 ")
            else:
                valid_input = True
        except ValueError:
            print('Invalid input. Enter a number')

    print(f"{age} is {is_even_or_odd(age)}")


def is_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
main()

valid_input = False
while not valid_input:
    try:
        print("priming read goes here")
        if "first false condition goes here" == True:
            print("error: you did this wrong"):
        elif "second false condition goes here" == True:
            print("error you also did this wrong"):
        else:
            valid_input = True
    except "name of error":
        print("error exception, this went wrong")
    except "name of second error":
        print("error exception this also went wrong")

print("continue with normal code here")


# second video

sqrt() # this square roots whatever number is inside:

F = (C * 1.8) + 32.0
# as opposed to:
F = celsius_to_fahrenheit(C)

def function_name(parameters):
    statement1
    statement2

    return __

"""FUNCTIONS SHOULD:
- do one thing only
- be readable
- be reusable
- be complete
- be not too long

should follow the SRP (single responsibility principle)
"""


''' MAIN FUNCTION SHOULD ESSENTIALLY LOOK LIKE THE WHOLE PROGRAM

def main():
    doStep1()
    doStep2()
    
def doStep1():
    dostep1part1
    dostep1part2
    
main()

(This is a good main function)

write main function and do all sub functions underneath the main (dont split up the main)
'''




