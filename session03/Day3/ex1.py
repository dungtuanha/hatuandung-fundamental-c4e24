password = str(input("enter yor password: "))

while len(password) <= 8:
    print("your password must have more than 8 characters")
    password = str(input("enter your password: "))
    if len(password) > 8:
        break

print("successed")