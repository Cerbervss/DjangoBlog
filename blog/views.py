from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def home(request):
    context = {
        "posts" : Post.objects.all()
    }
    return render(request, "blog/home.html", context)

def bloggers(request):
    context = {
        "title": "Utenti Attivi",
        "users": User.objects.all()
    }
    return render(request, "blog/users_list.html", context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-data"]
    paginate_by = 3

class LastPostListView(ListView):
    model = Post
    template_name = "blog/last_posts.html"
    context_object_name = "posts"
    queryset = Post.objects.all().order_by("-data")[:2]

    def get_context_data(self,**kwargs):
        context = super(LastPostListView,self).get_context_data(**kwargs)
        context['title'] = "Ultimi Post"
        return context

class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_post.html"
    context_object_name = "posts"
    ordering = ["-data"]
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get("username"))
        return Post.objects.filter(autore = user).order_by("-data")

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["titolo", "contenuto"]
    
    def form_valid(self, form):
        form.instance.autore = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["titolo", "contenuto"]
    
    def form_valid(self, form):
        form.instance.autore = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autore:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autore:
            return True
        return False
    
    
def about(request):
    return render(request, "blog/about.html", {"title": "About"})