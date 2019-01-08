#1. Connect database:
import mlab
from mongoengine import Document, StringField, IntField

mlab.connect()

#2. Define model:
class Movie(Document):
    title = StringField()
    img = StringField()
    link = StringField()
    rate = IntField()

movie_list = Movie.objects(rate__gte=9, title__icontains="aquaman")
for m in movie_list:
    print(m.title, m.rate)
# #3. Create Data:
# m = Movie(title="Aquaman",
#            link="https://www.imdb.com/title/tt1477834/",
#            rate=9.1)

# #4. Save Data
# m.save()

