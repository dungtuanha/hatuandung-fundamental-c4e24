from flask import Flask, render_template
app = Flask(__name__)

# templates rendering

@app.route("/characters")
def chracters():
    c = {
        "name": "Thanos",
        "img": "https://genknews.genkcdn.vn/2018/2/11/photo-0-15183674116352009609619.png",
        "link": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwi0qLDS1tbfAhVDdXAKHZSlAh0QjRx6BAgBEAU&url=http%3A%2F%2Fgamek.vn%2Ftai-sao-thanos-phai-la-nguoi-chien-thang-trong-avengers-infinity-war-20180211235034768.chn&psig=AOvVaw2nAXkWNhOc10ohscLvRk-W&ust=1546778832153556"
    }

    c_list = [
        {
           "name": "Thanos",
            "img": "https://genknews.genkcdn.vn/2018/2/11/photo-0-15183674116352009609619.png",
            "link": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwi0qLDS1tbfAhVDdXAKHZSlAh0QjRx6BAgBEAU&url=http%3A%2F%2Fgamek.vn%2Ftai-sao-thanos-phai-la-nguoi-chien-thang-trong-avengers-infinity-war-20180211235034768.chn&psig=AOvVaw2nAXkWNhOc10ohscLvRk-W&ust=1546778832153556" 
        },
        {
            "name": "Captain Marvel",
            "img": "https://genknews.genkcdn.vn/2018/2/11/photo-0-15183674116352009609619.png",
            "link": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwi0qLDS1tbfAhVDdXAKHZSlAh0QjRx6BAgBEAU&url=http%3A%2F%2Fgamek.vn%2Ftai-sao-thanos-phai-la-nguoi-chien-thang-trong-avengers-infinity-war-20180211235034768.chn&psig=AOvVaw2nAXkWNhOc10ohscLvRk-W&ust=1546778832153556"
        },
        {
            "name": "SpiderMan",
            "img": "https://genknews.genkcdn.vn/2018/2/11/photo-0-15183674116352009609619.png",
            "link": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwi0qLDS1tbfAhVDdXAKHZSlAh0QjRx6BAgBEAU&url=http%3A%2F%2Fgamek.vn%2Ftai-sao-thanos-phai-la-nguoi-chien-thang-trong-avengers-infinity-war-20180211235034768.chn&psig=AOvVaw2nAXkWNhOc10ohscLvRk-W&ust=1546778832153556"
        }
    ]
    return render_template("character_list.html", 
                            characters = c_list,
                            )



if __name__ == '__main__':
  app.run(debug=True)