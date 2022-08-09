# Django
from django import forms

# Models
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo', 'like','description')



class Comments(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = Comment
        fields = ('comments',)