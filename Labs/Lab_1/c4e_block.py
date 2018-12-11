from pymongo import MongoClient

#1. Connect to database server
uri = "mongodb://admin_dth:dungngovawater00@ds121575.mlab.com:21575/c4e24-lab1"
client = MongoClient(uri)

#2. Select database
db = client.get_database()

#3. Select collection
post_collection = db["posts"]

for post in post_collection.find():
    print(post)

# #4. Create document
# new_document = {
#     "title": "hnay troi VN thang" ,
#     "post": "minh di boi" ,
# }

# #5. Add document into collection
# post_collection.insert_one(new_document)

# #6. Close connection
# client.close()
