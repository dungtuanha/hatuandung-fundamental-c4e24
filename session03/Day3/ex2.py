password = str(input("enter yor password: "))

while password.isupper() or password.islower():
    print("your password must have both upper and lower character")
    password = str(input("enter your password: "))
    if not(password.islower()) and not(password.isupper()):
        break

print("successed")