from django import forms
from ckeditor.fields import RichTextField

from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=300, widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':"Title"}))
    class Meta:
        model = Post
        fields = ['title', 'thumbnail', 'author','content','category',]

