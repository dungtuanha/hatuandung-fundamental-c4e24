p1 = {
    "name": "dth",
    "city": "Ha Noi",
    "age": 18,
}

p2 = {
    "name": "Long",
    "city": "Ha Noi",
    "age": 18,
}

p3 = {
    "name": "Hoang",
    "city": "Ha Noi",
    "age": 18,
}

p_list = [p1, p2, p3]

print(p_list)

#p = p_list[0]
#print(p)

for p in p_list:
    print(p["name"])
    print(p["age"])
    print(p["city"])