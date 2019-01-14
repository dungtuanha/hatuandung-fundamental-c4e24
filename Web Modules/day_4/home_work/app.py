from flask import Flask, render_template, request, session, redirect
from models.add_bike import Bike
import mlab
from models.register import Register

mlab.connect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "very secret"

#NOTICE: this is a combination from 4 web's lessions, so pls start with "http://127.0.0.1:5000/register" :D

@app.route("/new_bike", methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("bike_rental.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]
        new_bike = Bike(model=model, fee=fee, image=image, year=year)
        new_bike.save()
        return "Car rendered successful" and redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login_form.html")
    elif request.method == "POST":
        form = request.form 
        username = form["username"]
        password = form["password"]

        found_user = Register.objects(username=username, password=password).first()
        if found_user is None:
            return "User not found"
        elif found_user.password != password:
            return "Invalid password"
        else:
            session["token"] = username
            next = request.args.get("?next")
            if next is None or next == "":
                return redirect("/new_bike")
            else:
                return redirect("/" + next)

@app.route('/register', methods = ['POST', 'GET'])
def register():
  if request.method == 'POST':
    nick = request.form

    real_name = nick['real_name']
    email = nick['email']
    username = nick['username']
    password = nick['password']

    r = Register(username = username,
                 password = password)
    
    r.save() 

    return redirect("/login")
  else:
    return render_template('register.html')


if __name__ == '__main__':
  app.run(debug=True)