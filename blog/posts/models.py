# Django
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    like = models.CharField(max_length=255, blank='true')
    description = models.CharField(max_length=255, blank='true')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comments = models.CharField(max_length=255)

    def __str__(self):
        """Return post and comments."""
        return '{} por @{} para @{}'.format(self.comments, self.post.user.username, self.post.title)