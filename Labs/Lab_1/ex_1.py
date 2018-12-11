from pymongo import MongoClient

uri = "mongodb://admin_dth:dungngovawater00@ds121575.mlab.com:21575/c4e24-lab1"
client = MongoClient(uri)

db = client.get_database()

post_collection = db["account"]

account = [
    {
        "username": "dungtuanha",
        "email": "dungtuanha@gmail.com",
        "phone": "094859674",
        "password": "hatuandung",
        "yob": "29/06",
    },

    {
        "username": "tranthanhlong",
        "email": "long@gmail.com",
        "phone": "091312312",
        "password": "adhasdadas",
        "yob": "25/05"
    },

    {
        "username": "nguyenminhhoang",
        "email": "asdadsad@gmail.com",
        "phone": "0913123313",
        "password": "hasdhdsad",
    }
]

for i in range(len(account)):
    post_collection.insert_one(account[i])

for acc in account:
    print(acc)

client.close()