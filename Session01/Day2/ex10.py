a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b*b - 4*a*c
print(delta)

if delta < 0:
    print("no solution")
elif delta == 0:
    print("1 solution")
    x = -b / (2*a)
    print("x = %f" %x)
else:
    print("2 solutions")
    x1 = (-b + delta**(1/2)) / 2*a
    x2 = (-b - delta**(1/2)) / 2*a
    print("x1 = %f" %x1)
    print("x2 = %f" %x2)
