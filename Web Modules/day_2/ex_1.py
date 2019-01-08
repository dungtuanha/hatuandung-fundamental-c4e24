from flask import Flask,render_template
app = Flask(__name__)

@app.route("/names")
def names():
    name_list = ["Huy", "Quan", "Huong", "Long", "Hoang", "Ha", "Dung"]
    return render_template("names.html",
                            names = name_list)

foods_list = [
        {
            "name": "Fried Chicken",
            "img": "https://znews-photo.zadn.vn/w660/Uploaded/tmuitg/2017_11_22/20171121163837.jpg",
            "link": "https://www.foody.vn/ha-noi/ga-ran-kuc-cu-tran-duy-hung",
            "id": "mfIgYdJCwUA"
        },
        {
            "name": "Pho",
            "img": "https://ichef.bbci.co.uk/food/ic/food_16x9_448/recipes/chicken_pho_97726_16x9.jpg",
            "link": "https://www.foody.vn/ha-noi/pho-1-ly-quoc-su-nguyen-hong",
            "id": "ftsQYS1fkOs"
        },
        {
            "name": "Bun Dau",
            "img": "https://images.foody.vn/res/g71/706548/prof/s576x330/foody-mobile-foody-chi-pheo-bun-d.jpg",
            "link": "https://www.foody.vn/ha-noi/bun-dau-goc-da",
            "id": "za17nKcK6_w"
        },
    ]
     
@app.route("/food_items")
def foods():
        return render_template("foods.html",
                                foods = foods_list)

@app.route("/food_detail/<int:index>")
def food_detail(index):
    food = foods_list[index]
    return render_template("food_detail.html",
                            food = food)

if __name__ == '__main__':
  app.run(debug=True)