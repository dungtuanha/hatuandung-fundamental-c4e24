import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds149744.mlab.com:49744/login

host = "ds149744.mlab.com"
port = 49744
db_name = "login"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())