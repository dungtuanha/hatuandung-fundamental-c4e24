dic = {
    "name": "htd",
    "age": 18,
    "school": "USTH",
    "status": "offline",
}

print(*dic)
guess = input("What do you want to know about me? ")

while True:
    if guess in dic:
       print(dic[guess])
       break
    else:
        print("Wrong key")
        guess = input("What do you want to know about me? ")
        