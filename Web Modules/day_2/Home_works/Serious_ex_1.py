import mlab
from mongoengine import Document, StringField, EmailField, DynamicField 
from flask import Flask, render_template, request
app = Flask(__name__)

mlab.connect()

class Register(Document):
    rname = StringField()
    email = EmailField()
    uname = StringField()
    psw = DynamicField()

@app.route('/register', methods = ['POST', 'GET'])
def register():
  if request.method == 'POST':
    nick = request.form

    real_name = nick['real_name']
    email = nick['email']
    user_name = nick['user_name']
    password = nick['password']

    r = Register(real_name = real_name,
                email = email,
                user_name = user_name,
                password = password)
    r.save() 

    return "Welcome"
  else:
    return render_template('register.html')

  

                            

if __name__ == '__main__':
  app.run(debug=True)