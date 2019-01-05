from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")   #router
def home():   #view function
    ab_list = ["a", "b", "c", "d", "e"]
    characters = {
        "name": "AQUAMAN",
        "company": "DC Comic",
        "image": "https://znews-photo.zadn.vn/w860/Uploaded/spuocaw/2018_12_21/aquaman12801543622354275_960w.jpg",
        "abilities": ["a", "b", "c", "d", "e"],
    }
    c = "AQUAMAN"
    comp = "DC Comic"
    img = "https://znews-photo.zadn.vn/w860/Uploaded/spuocaw/2018_12_21/aquaman12801543622354275_960w.jpg"
    return render_template("home.html", 
                                        characters = charaters)  #serve html


@app.route("/c4e")
def c4e():
    return "code for everyone 24"

@app.route("/hi/<name>")
def say_hi(name):
    print(name)

@app.route("/add/<num1>/<num2>")
def add(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    s = str(num1 + num2)
    return s

if __name__ == "__main__":
    app.run(debug=True)