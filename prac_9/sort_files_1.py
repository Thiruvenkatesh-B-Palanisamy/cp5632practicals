import os


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        new_folder_name = filename.split('.')[-1]
        try:
            os.mkdir(new_folder_name)
        except FileExistsError:
            pass
        print("{}/{}".format(new_folder_name, filename))
        os.rename(filename, "{}/{}".format(new_folder_name, filename))


print("Hurray your files sorted")
main()
