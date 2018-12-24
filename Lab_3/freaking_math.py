from random import *

x = randint(0, 9)
y = randint(0, 9)
error = randint(-1, 1)
pt_list = ["+", "-", "*", "/"]
pt = choice(pt_list)

if pt == "+":
    r = x + y + error
elif pt == "-":
    r = x - y + error
elif pt == "*":
    r = x * y + error
elif pt == "/":
    r = x / y + error

print(f"{x} {pt} {y} = {r}")

user_answer = input("Y/N? ").upper()

if error == 0:
    if user_answer == "Y":
        print("yay")
    elif user_answer == "N":
        print('wrong')
else:
    if user_answer == "Y":
        print("wrong")
    elif user_answer == "N":
        print('yay')