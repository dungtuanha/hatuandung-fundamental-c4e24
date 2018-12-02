print("Hello my name is Dung and there are my sheeps sizes:")
sizes = [5, 7, 300, 90, 2, 50, 75]
print(sizes)

print("**************************************************************")

n = max(sizes)
print("Now my biggest sheep has sizez ", n, end =" ")
print("lets shear it")

print("**************************************************************")

sizes.remove(n)
print("After shearing, here is my flock: ")
print(sizes)

print("**************************************************************")

for i in range(len(sizes)):
    sizes[i] = sizes[i] + 50
print("One month is passed, now here is my flock: ")
print(sizes)

print("**************************************************************")

j = int(input("How many months do you want the programs to pass? "))
for i in range(1,j+1):
    print("MONTH " , i , end = ":")
    print()

    for k in range(len(sizes)):
        sizes[k] = sizes[k] + 50
    print("One month is passed, now here is my flock: ")
    print(sizes)

    n = max(sizes)
    print("Now my biggest sheep has sizez ", n, end =" ")
    print("lets shear it")
    
    sizes.remove(n)
    print("After shearing, here is my flock: ")
    print(sizes)
    print()

sizes_sum = sum(sizes)
print("My flock has sizes in total: ", sizes_sum)
money = sizes_sum * 2
print("I would get ", sizes_sum, end = " * 2$ = ")
print(money)

