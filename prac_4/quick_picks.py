import random

set_of_numbers = 6
max_number = 45
min_number = 1


def main():
    quick_pick = quick_pick_validation()

    for pick in range(quick_pick):
        quick_picks = []
        for number in range(set_of_numbers):
            numbers = random.randint(min_number, max_number)
            while numbers in quick_picks:
                numbers = random.randint(min_number, max_number)
            quick_picks.append(numbers)
        quick_picks.sort()

        print(" ".join("{:2}".format(pick) for pick in quick_picks))


def quick_pick_validation():
    user_pick = int(input("How many quick picks ?"))
    while user_pick <= 0:
        user_pick = int(input("Invalid quick pick\nHow many quick picks ?"))
    return user_pick


main()


