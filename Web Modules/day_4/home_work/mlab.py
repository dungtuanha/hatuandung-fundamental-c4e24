import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds255924.mlab.com:55924/bike_rental

host = "ds255924.mlab.com"
port = 55924
db_name = "bike_rental"
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