from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name='about'),
    path('add-post/', views.AddPost.as_view(), name= 'addPost'),
    path('post-detail/<str:pk>/', views.PostDetail.as_view(), name="postDetail"),
    path('all-posts/', views.PostList.as_view(), name='allPosts'),
    path('add-comment/',views.addComment, name="addComment"),
]