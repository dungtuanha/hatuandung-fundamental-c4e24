from flask import Flask, render_template, request, session, redirect
from models.character import Character
from models.user import User
import mlab

mlab.connect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "very secret"


@app.route('/add_character', methods=['GET', 'POST'])
def character():
    #send form (GET)
    if request.method =="GET":
        return render_template("character_form.html")
    elif request.method == "POST":
        #save (POST)
        form = request.form
        image = form["image"]
        name = form["name"]
        rate = form["rate"]
        new_character = Character(name=name, image=image, rate=rate)
        new_character.save()
        return "GOTCHA" 

@app.route("/characters", methods=['GET', 'POST'])
def character_list():
    if "token" in session:
        characters = Character.objects()
        return render_template("character_list.html", character_list = characters)
    else:
        return redirect("/login?next=/characters")

@app.route("/characters/<id>")
def id(id):
    #character = Character.objects(id=id).first()
    character = Character.objects().with_id(id)
    if character is None:
        return "Not Found"
    else:
        return render_template("id.html", character=character)


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login_form.html")
    elif request.method == "POST":
        form = request.form 
        username = form["username"]
        password = form["password"]

        found_user = User.objects(username=username).first()
        if found_user is None:
            return "User not found"
        elif found_user.password != password:
            return "Invalid password"
        else:
            session["token"] = username
            next = request.args.get("?next")
            if next is None or next == "":
                return "Login succesfully"
            else:
                return redirect("/" + next)

@app.route("/logout")
def logout():
    del session["token"]
    return redirect("/login")

@app.route("/posts")
def posts():
    if "token" not in session:
        return redirect("/login?next=/posts")
    else:
        username = session["token"]


if __name__ == '__main__':
  app.run(debug=True)