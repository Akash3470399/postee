from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('add-post/', views.AddPost.as_view(), name= 'addPost'),
    path('post-detail/<str:pk>/', views.PostDetail.as_view(), name="postDetail"),
    path('all-posts/', views.PostList.as_view(), name='postList'),
]