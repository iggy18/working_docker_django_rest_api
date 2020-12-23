from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# create home page view extend list view
class HomePageView(ListView):
    template_name = "home.html"
    model = Post

# add detail view
class DetailView(DetailView):
    template_name = "post_detail.html"
    model = Post

class CreateBlogView(CreateView):
    template_name = "create_blog.html"
    model = Post
    fields = ['author', 'title', 'body']

class BlogUpdateView(UpdateView):
    template_name = "update_blog.html"
    model = Post
    fields = ['title', 'body']


class DeleteBlogView(DeleteView):
    template_name = "delete_blog.html"
    model = Post
    success_url = reverse_lazy('home')
