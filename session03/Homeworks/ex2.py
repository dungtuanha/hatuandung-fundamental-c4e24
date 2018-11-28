n = int(input("enter the number: "))

a = int(input("guess my number(1-100): "))

while a != n:
    
    if a > n:
        print("a little too large :(")
    elif a < n:
        print("a little too small :(")
    
    a = int(input("try again: "))

    if a == n:
        print("bingo")
        break
