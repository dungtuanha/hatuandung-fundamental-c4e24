clothes = ["T-Shirt", "Sweater"]

while True:
    guess = str(input("Welcome to our shop, what do you want (C, R, U, D, E)? ")).upper()
    
    if guess == "R":
        print("Our items: ", end = "")        
        for i in range(len(clothes)):
            print(clothes[i], end = ", ")
        print()
    elif guess == "C":
        new_item = input("enter new item: ")
        clothes.append(new_item)
        print("Our items: ", end = "")
        print(clothes)
    elif guess == "U":
        pos = int(input("update pos? "))
        new_item = input("new item? ")
        clothes[pos-1] = new_item
        print("Our items: ", end = "")
        print(clothes)
    elif guess == "D":
        del_pos = int(input("delete position? "))
        clothes.pop(del_pos - 1)
        print(clothes)
    elif guess == "E":
        break
