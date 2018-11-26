print("Welcome to the system, please enter your username and password")


username = str(input("Username: "))

if username == str('hatuandung'):
    password = str(input("Password: "))
    if password == str('hatuandung'):
        print("Welcome")
    else:
        print("Wrong password, pls try again")
else:
    print("Wrong username, pls try again")

