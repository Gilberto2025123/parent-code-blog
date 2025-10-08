from django.shortcuts import render
from django.views import generic
from .models import Post, Category, Comment


# Create your views here.
class PostList(generic.ListView):
    model = Post

