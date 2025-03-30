from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    

