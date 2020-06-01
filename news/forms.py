from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('topic', 'about', 'content', 'image', 'source')


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('topic', 'about', 'content', 'source')


