# Update, Delete
# Atomic
import mlab
from models.character import Character


mlab.connect()

character = Character.objects().with_id("5c34a7d7a3dead29543d463f")

# print(character)
# character.update(set__rate=4, set__name="SuperMan")     # set__inc__
# character.reload()

character.delete()

# 1. Update
# 1.1 Read Document
# 1.2 Update Document

# 2. Delete
# 2.1 Read Document
# 2.2 Delete Document