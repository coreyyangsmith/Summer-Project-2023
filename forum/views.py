from django.shortcuts import render, get_object_or_404
from .models import User, Category, Thread, Post, Neighbourhood
from django.views.generic import *
from django.urls import reverse


def index(request):
    context = {}
    return render(request, "index.html", context)


# Uses django generic views and points to template files
# just to show the backend functionality, will need to be refactored
# later and potentially use an API (djangorestframework) to send this data
# to the frontend (React) to be rendered.

class NeighbourhoodListView(ListView): # TODO Corey | Add User Auth, filter view based on user permission
    model = Neighbourhood

class CategoryListView(ListView):
    model = Category
    def get_queryset(self):
        # Get path to neighbourhood, to find FK ref for category
        code = self.request.path
        code = code[:-1]
        code = code.rsplit('/', 1)[-1]         

        self.neighbourhood = get_object_or_404(Neighbourhood, code=code)
        return Category.objects.filter(neighbourhood=self.neighbourhood)

class ThreadListView(ListView):
    model = Thread
    def get_queryset(self):
        # Get path to neighbourhood, to find FK ref for category
        code = self.request.path
        code = code[:-1]
        code = code.rsplit('/', 1)[-1]               

        self.category = get_object_or_404(Category, id=code)
        return Thread.objects.filter(category=self.category)    

class ThreadDetailView(DetailView): # TODO Corey | Add Detail View for Threads(CRUD for Thread)
    model = Thread

class PostListView(ListView):
    model = Post
    print("post view")

    def get_queryset(self):
        # Get path to neighbourhood, to find FK ref for category
        code = self.request.path
        code = code[:-1]
        code = code.rsplit('/', 1)[-1]      

        self.thread = get_object_or_404(Thread, id=code)
        return Post.objects.filter(thread=self.thread)        

class PostDetailView(DetailView): # TODO Corey | Add Detail View for Posts (CRUD for Thread)
    model = Post        