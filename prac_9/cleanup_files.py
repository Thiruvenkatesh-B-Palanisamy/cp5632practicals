"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            try:
                os.rename(full_name, new_name)
            except FileExistsError:
                pass


def get_fixed_filename(filename):
    new_name = ""

    if "_" not in filename:
        for e, letter in enumerate(filename):
            if e > 0:
                if letter.isupper():

                    new_name += "_" + letter
                    print(new_name)
                else:
                    new_name += letter
            else:
                new_name += letter
    new_name.replace(" ", "_").replace(".TXT", ".txt")

    return new_name


main()
