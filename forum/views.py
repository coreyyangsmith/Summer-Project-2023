from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import *
from django.urls import reverse
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def index(request):
    context = {}
    return render(request, "index.html", context)


## API Views for RESTful Calls
#-- Categories --#
@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':
        data = Category.objects.all()
        serializer = CategorySerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

## TODO categories_detail

#-- Thread --#
@api_view(['GET', 'POST'])
def threads_list(request):
    if request.method == 'GET':
        data = Thread.objects.all()
        serializer = ThreadSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

## TODO threads_detail

#-- Post --#
@api_view(['GET', 'POST'])
def posts_list(request):
    if request.method == 'GET':
        data = Post.objects.all()
        serializer = PostSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

## TODO posts_detail


# Uses django generic views and points to template files
# just to show the backend functionality, will need to be refactored
# later and potentially use an API (djangorestframework) to send this data
# to the frontend (React) to be rendered.

class CommunityListView(ListView): # TODO Corey | Add User Auth, filter view based on user permission
    model = Community

class CommunityDetailView(DetailView):
    model = Community    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        pk = self.kwargs['pk']              
        context["community"] = Community.objects.get(pk=pk)      
        return context      

class CategoryListView(ListView):
    model = Category
    def get_queryset(self):
        # Get path to neighbourhood, to find FK ref for category
        code = self.request.path
        code = code[:-1]
        code = code.rsplit('/', 1)[-1]         

        self.community = get_object_or_404(Community, code=code)
        return Category.objects.filter(community=self.community)

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
    def get_queryset(self):
        # Get path to neighbourhood, to find FK ref for category
        code = self.request.path
        code = code[:-1]
        code = code.rsplit('/', 1)[-1]      

        self.thread = get_object_or_404(Thread, id=code)
        return Post.objects.filter(thread=self.thread)        

class PostDetailView(DetailView): # TODO Corey | Add Detail View for Posts (CRUD for Thread)
    model = Post        