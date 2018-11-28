n = int(input("enter your number: "))

s = 1

while n // 10 != 0:
    s = s+1
    n = n // 10

print("Digit count: ", end = (""))
print(s)