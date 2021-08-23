"""CP1404 PRACTICAL 3"""


def main():
    score = float(input("Enter score: "))
    return_result(score)


def return_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()