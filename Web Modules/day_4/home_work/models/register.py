from mongoengine import *

class Register(Document):
    username = StringField()
    password = StringField()