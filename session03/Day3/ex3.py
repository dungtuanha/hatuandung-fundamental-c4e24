things = ["Tran" , "Thanh" , "Long"]
n = int(input("enter an index: "))

while n >= 3:
    print("try again")
    n = int(input("enter an index: "))
    if n < 3:    
        print(things[n])
        break