yob_str = input("YOB? ")

while yob_str != int:
    yob_str = input("YOB? ")
    if yob_str.isdigit():
        break

yob = int(yob_str)
age = 2018 - yob
print(age)