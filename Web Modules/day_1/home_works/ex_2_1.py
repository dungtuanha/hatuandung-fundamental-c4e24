# Without using render_template() function
from flask import Flask
app = Flask(__name__)

@app.route("/bmi/<int:w>/<int:h>")
def bmi(w,h):
    # h = float(input("Enter your height:(cm)"))
    # w = float(input("Enter your weight:(kg)"))
    BMI = w/(h/100*h/100)
    if BMI < 16:
        return ("Your BMI is: " + str(BMI) + " You're Severely Underweight")
    elif BMI < 18.5:
        return ("Your BMI is: " + str(BMI) + " You're Underweight")
    elif BMI < 25:
        return ("Your BMI is: " + str(BMI) + " You're Normal")
    elif BMI < 30:
        return ("Your BMI is: " + str(BMI) + " You're Overweight")
    else:
        return ("Your BMI is: " + str(BMI) + " You're Obese")
    

if __name__ == '__main__':
  app.run(debug=True)