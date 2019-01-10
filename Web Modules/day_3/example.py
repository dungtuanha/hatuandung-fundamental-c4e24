from flask import Flask, render_template, request
from models.character import Character
import mlab

mlab.connect()
app = Flask(__name__)


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
    characters = Character.objects()
    return render_template("character_list.html", character_list = characters)

@app.route("/characters/<id>")
def id(id):
    #character = Character.objects(id=id).first()
    character = Character.objects().with_id(id)
    if character is None:
        return "Not Found"
    else:
        return render_template("id.html", character=character)


    

if __name__ == '__main__':
  app.run(debug=True)