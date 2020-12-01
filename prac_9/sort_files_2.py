import os


def main():
    folder_category_dict = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        new_folder_name = filename.split('.')[-1]
        if new_folder_name not in folder_category_dict:
            category = input("What category would you like to sort {} files into? ".format(new_folder_name))

            folder_category_dict[new_folder_name] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(folder_category_dict[new_folder_name], filename))


print("Hurray your files sorted")
main()
