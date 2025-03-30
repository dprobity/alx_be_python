from django.contrib.auth.models import User
from blog.models import BlogPost, Comment

# Create or get a user
user, created = User.objects.get_or_create(username='testuser')
if created:
    user.set_password('testpass123')
    user.first_name = 'Test'
    user.last_name = 'User'
    user.save()

print(f"Using user: {user.username} (ID: {user.id})")

# Create 3 blog posts
post1 = BlogPost.objects.create(author=user, title='First Post', content='This is the first blog post.')
post2 = BlogPost.objects.create(author=user, title='Second Post', content='More content here.')
post3 = BlogPost.objects.create(author=user, title='Third Post', content='Even more bloggy stuff.')

print("Created 3 blog posts.")

# Create 5 comments on the first post
for i in range(1, 6):
    Comment.objects.create(
        post=post1,
        author=user,
        content=f"This is comment #{i} on the first blog post."
    )

print("Added 5 comments to the first post.")
