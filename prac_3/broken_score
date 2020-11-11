import random


def main():

    score = float(input("Enter score: "))
    score_validation = check_score(score)
    print("{} is {}".format(int(score), score_validation))
    score = random.randrange(101)
    score_validation = check_score(score)
    print("{} is {}".format(int(score), score_validation))


def check_score(score):

    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif 49 < score < 90:
        return "Passable"
    elif 89 < score < 101:
        return "Excellent"
    elif score < 50:
        return "Bad"


main()


