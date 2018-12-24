from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 9)
    y = randint(1, 10)
    error = randint(-1,1)
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
    return [x, y, pt, r]

def check_answer(x, y, pt, r, user_choice):
    
    a = generate_quiz()
    x = a[0]
    y = a[1]
    pt = a[2]
    r = a[3]

    if pt == "+":
        error = r - x -y
    elif pt == "-":
        error = r - x + y
    elif pt == "*":
        error = r - x * y
    elif pt == "/":
        error = r - x / y

    if error == 0:
        if user_choice == True:
            return True
        elif user_choice == False:
            return False
    else:
        if user_choice == True:
            return False
        elif user_choice == False:
            return True
