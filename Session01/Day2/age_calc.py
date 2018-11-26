yob = int(input("enter your yob: "))
age = 2018 - yob
print("Your age: %d" %age)

if age < 10:
    print("baby")
elif age < 18:
    print("teenager")     
else:
    print("adult")

print("bye")