from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from gdstorage.storage import GoogleDriveStorage


gd_storage = GoogleDriveStorage()


class Post(models.Model):
    title = models.CharField(max_length = 250)
    thumbnail = models.ImageField(upload_to = 'images/', null = True, blank = True,storage=gd_storage)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank = True, null= True)
    category = models.CharField(max_length=250,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:postDetail", kwargs={"pk": self.pk})
    


class Comment(models.Model):
    text = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp =  models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text