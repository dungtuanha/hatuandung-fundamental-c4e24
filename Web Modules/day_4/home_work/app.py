from flask import Flask, render_template, request, session, redirect
from models.add_bike import Bike
import mlab

mlab.connect()
app = Flask(__name__)

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
        return redirect("/new_bike")


if __name__ == '__main__':
  app.run(debug=True)