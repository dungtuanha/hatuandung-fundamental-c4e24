import mlab
from models.user import User
from models.post import Post

mlab.connect()

# a_random_user = User.objects(username="hatuandung").first()
# if a_random_user is None:
#     print("User not found")
# else:
#     new_post = Post(title="hatuandung",
#                     content="hoho",
#                     owner=a_random_user)
#     new_post.save()
#     print("Done saving")


#Post -> Owner
# for post in Post.objects():
#     print(post.title)
#     print(post.owner.username)

#Owner -> Posts
user = User.objects(username="dungtuanha").first()
posts = Post.objects(owner=user)
for post in posts:
    print(post.title)