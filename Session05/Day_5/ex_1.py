salary = [
    {
        "name": "Huy",
        "hours": 25,
        "VND/hour": 20,
    } ,

    {
        "name": "Quan",
        "hours": 30,
        "VND/hour": 30,
    } ,

    {
        "name": "Duc",
        "hours": 15,
        "VND/hour": 25,
    }
]

wage_list = [p["VND/hour"] * p["hours"] for p in salary]
total = sum(wage_list)
print(wage_list)
print(total)

#Huy = salary[0]
#Quan = salary[1]
#Duc = salary[2]

#Huy_sal = Huy["hours"] * Huy["VND/hour"]
#Quan_sal = Quan["hours"] * Quan["VND/hour"]
#Duc_sal = Duc["hours"] * Duc["VND/hour"]

#print("Huy:", Huy_sal)
#print("Quan:", Quan_sal)
#print("Duc:", Duc_sal)