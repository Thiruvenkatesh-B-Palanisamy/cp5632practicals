"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subjects(data)


def get_data():
    data = []
    input_file = open(FILENAME)
    for line in input_file:

        line = line.strip()
        parts = line.split(',')
        data.append(parts)
    input_file.close()
    return data


def display_subjects(data):
    for subject_data in data:
        print("{} is taught by {:12} and has {:3} students".format(subject_data[0], subject_data[1], subject_data[2]))


main()

