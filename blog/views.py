from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


def index(request):
    recent_posts = Post.objects.all().order_by("-timestamp")[0:3]
    top_posts = Post.objects.all()[0:3]
    contex = {'recent_posts':recent_posts, "top_posts":top_posts}
    return render(request, 'blog/index.html', contex)

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:home')

# def AddPost(request):
#     form = PostForm()
#     if request.method == "POST":
#         print(request.POST)
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             print(form.errors)

#     return render(request, 'blog/post_form.html', {"form":form})


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
