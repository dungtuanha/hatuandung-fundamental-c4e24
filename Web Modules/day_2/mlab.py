import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds159344.mlab.com:59344/moviedb

host = "ds159344.mlab.com"
port = 59344
db_name = "moviedb"
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