import wikipedia

user_input = wikipedia.page(input("enter page title or search phrase:\n>>>"))
while user_input != "":
    try:
        print("{}\n{}\n{}".format(user_input.title, user_input.summary, user_input.url))
        user_input = wikipedia.page(input("enter page title or search phrase:\n>>>"))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)


