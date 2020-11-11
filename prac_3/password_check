min_length = 6


def main():

    password = password_check()
    password_hide = password_hider(password)
    print("Your password is: '{}'".format(password_hide))


def password_hider(password):
    password_hide = len(password) * "*"
    return password_hide


def password_check():
    password = input("Enter your password: ")
    while len(password) < min_length:
        password = input("password length should be minimum 6 characters!\nEnter your password: ")
    return password


main()

