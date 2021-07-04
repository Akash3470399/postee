from django import forms
from ckeditor.fields import RichTextField
from django.db.models import fields

from .models import Comment, Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=300, widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':"Title"}))
    category = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category'}))
    class Meta:
        model = Post
        fields = ['title', 'thumbnail','content','category',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author','related_post']




