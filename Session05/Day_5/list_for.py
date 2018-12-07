person = {
    "name": "dth",
    "city": "Ha Noi",
    "age": 18,
    "books": ["Nicolas", "Diary of a wimpy kid"] ,
}

#for x in person:
    #print(x)

#for v in person.values():
    #print(v)

#for k,v in person.items():
    #print(k,v)

print(person["books"])

books = person["books"]
print(books)

for b in person["books"]:
    print(b)

print(person["books"][1])