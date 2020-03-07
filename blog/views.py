from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import BlogPost

class BlogIndex(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = 'blog_posts'
    ordering = ['-date_posted']


class BlogDetail(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'
    context_object_name = 'blog'


class BlogNew(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'blog/new.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)