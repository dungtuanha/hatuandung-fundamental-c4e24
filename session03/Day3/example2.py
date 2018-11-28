print("Here your 3 favorite thing")
things = ["Dit" , "Me" , "Long"]
print(*things, sep = ", ")

thing_4 = input("do you want to add sth? ")
things.append(thing_4)
print(*things, sep = ", ")


