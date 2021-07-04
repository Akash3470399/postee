from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import json
from .models import Post, Comment
from .forms import PostForm,CommentForm


def index(request):
    recent_posts = Post.objects.all().order_by("-timestamp")[0:3]
    top_posts = Post.objects.all()[0:3]
    contex = {'recent_posts':recent_posts, "top_posts":top_posts}
    return render(request, 'blog/index.html', contex)

def addComment(request):
    comment_dict = json.load(request)
    author = User.objects.get(id = comment_dict['author'])
    post = Post.objects.get(id = comment_dict['related_post'])
    comment = Comment(author=author, text=comment_dict['text'],related_post=post)
    comment.save()
    return JsonResponse({"text":comment_dict['text'], 'author':author.username})


def about(request):
    return render(request, 'blog/about.html')

class AddPost(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    model = Post
    form_class = PostForm
    # success_url = reverse_lazy('blog:home') #specify success_url or define get_absolute_url method in model

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        comments = Comment.objects.all().filter(related_post = kwargs['object'].id)
        context = super().get_context_data(**kwargs)
        context['comments'] = comments
        return context

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

