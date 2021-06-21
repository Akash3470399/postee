from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 250)
    thumbnail = models.ImageField(upload_to = 'images/', null = True, blank = True,)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank = True, null= True)
    category = models.CharField(max_length=250,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title