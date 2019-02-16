from flask import *
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/love')
def love():
  love_list = [
    "If you have only one smile in you give it to the people you love.",
    "There is only one happiness in this life, to love and be loved.",
    "You look amazing out there.",
    "They invented hugs to let people know you love them without saying anything.",
    "If you love someone, let them know.",
    "Don't ever forger a thing called love.",
    "Everyone needs to be loved",
  ]
  for j in range(len(love_list)):
    j = randint(0, len(love_list) - 1 )
    love = love_list[j]

  li = [ "love.html" , "love1.html" , "love2.html" , "love3.html", "love4.html" ]
  for _ in range (len(li)):
    i = randint (0, len(li) -1)
    l = li[i]
  return render_template(l, love = love)

@app.route('/haha')
def haha():
  haha_list = [
    "No man has a good enough memory to be a successful liar.",
    "There are only three things women need in life: food, water, and compliments.",
    "Laugh and the world laughs with you, snore and you sleep alone.",
  ]
  for j in range(len(haha_list)):
    j = randint(0, len(haha_list) - 1 )
    haha = haha_list[j]

  li = [ "haha.html" , "haha1.html" , "haha2.html"]
  for _ in range (len(li)):
    i = randint (0, len(li) -1)
    l = li[i]
  return render_template(l, haha = haha)

@app.route('/yay')
def yay():
  yay_list = [
    "Be happy for this moment. This moment is your life.",
    "Life is full of happiness and tears; be strong and have faith.",
    "The best way to pay for a lovely moment is to enjoy it.",
    "Happiness lies in the joy of achievement and the thrill of creative effort.",
    "The most simple things can bring the most happiness.",
    "Happiness held is the seed; Happiness shared is the flower.",
  ]
  for j in range(len(yay_list)):
    j = randint(0, len(yay_list) - 1 )
    yay = yay_list[j]

  li = [ "yay.html" , "yay1.html" , "yay2.html" , "yay3.html" , "yay4.html", "yay5.html"]
  for _ in range (len(li)):
    i = randint (0, len(li) -1)
    l = li[i]
  return render_template(l, yay = yay)

@app.route('/sad')
def sad():
  sad_list = [
    "Be happy for this moment. This moment is your life."
    "The good times of today, are the sad thoughts of tomorrow.",
    "Let my soul smile through my heart and my heart smile through my eyes, that I may scatter rich smiles in sad hearts.",
    "Tears come from the heart and not from the brain.",
    "Don’t Let Yesterday Take Up Too Much Of Today.",
    "You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.",
    "Remember Life Is All About Those Moment You Never Forget",
    "It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.",
    "Dreams Come True When You Follow Your Heart.",
  ]
  for j in range(len(sad_list)):
    j = randint(0, len(sad_list) - 1 )
    sad = sad_list[j]

  li = [ "sad.html" , "sad1.html" , "sad2.html" , "sad3.html" ]
  for _ in range (len(li)):
    i = randint (0, len(li) -1)
    l = li[i]
  return render_template(l, sad = sad)

@app.route('/angry')
def angry():
  angry_list = [
    "For every minute you remain angry, you give up sixty seconds of peace of mind.",
    "To be angry is to revenge the faults of others on ourselves.",
    "We are not an angry person. It's just the roles We do that impact Our personality.",
    "When angry, count to four; when very angry, swear.",
    "Every time you get angry, you poison your own system.",
    "No person is important enough to make you angry.",
    "Whatever Happens, We'll Be Ok ",
  ]
  for j in range(len(angry_list)):
    j = randint(0, len(angry_list) - 1 )
    angry = angry_list[j]


  li = [ "angry.html" , "angry1.html", "angry2.html", "angry3.html"]
  for _ in range (len(li)):
    i = randint (0, len(li) -1)
    l = li[i]
  return render_template(l, angry = angry)


if __name__ == '__main__':
  app.run(debug=True) 
    