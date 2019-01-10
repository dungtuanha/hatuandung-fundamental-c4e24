import mlab
from models.river import River

mlab.connect()

Africa_river_list = River.objects(continent__icontains="Africa")
print("all river in Africa: ", end="")
for river in Africa_river_list:
    print(river.name, end=", ")
print()
print()

S_America_river_list = River.objects(continent__icontains="S. America", length__lt=1000)
print("all river in S.America with length less than 1000km: ", end="")
for river in S_America_river_list:
    print(river.name, end=", ")