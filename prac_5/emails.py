def main():
    store_email_name_dict = {}
    email = input("Email: ")
    while email != "":
        name = name_extractor_from_email(email)
        name_valid = input("Is your name {}? (y/n)".format(name)).lower()
        if name_valid == "y" and name_valid != "":
            store_email_name_dict[email] = name
            email = input("Email: ")
        else:
            name = input("Name: ")
            store_email_name_dict[email] = name
            email = input("Email: ")

    for email, name in store_email_name_dict.items():
        print("{} ({})".format(name, email))


def name_extractor_from_email(email):
    email_split = email.split("@")[0]
    first_part = email_split.split(".")
    name = " ".join(first_part).title()
    return name


main()

