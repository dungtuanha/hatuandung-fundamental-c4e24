n = int(input("n: "))

i = 1
while i <= n:
    print("x", end = " ")
    i = i +1
    if i <= n:
        print("*", end = " ")
        i = i + 1
    else:
        exit()    