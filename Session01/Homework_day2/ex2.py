kg = int(input("weight: "))
cm = int(input("height: "))

m = cm*0.01

BMI = kg / (m*m)

if BMI < 16:
    print("severely underweight")
elif BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal")
elif BMI < 30:
    print("overweight")
else:
    print("Obese")

