from django.shortcuts import render
from .models import *
from .serializers import *
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
def index(response, id):
    user = User.objects.get(id=id)
    return render(response, 'main/display.html', {"user":user})

def home(request):
    return render(request, 'main/home.html',{})

def vote(request, comm_code):
    _, created = Vote.objects.get_or_create(
                    neighbourhood_key = Neighbourhood.objects.get(code=comm_code),
                    vote_time=timezone.now(),
                    created_at=timezone.now(),
                    updated_at=timezone.now())
    return render(request, 'main/home.html',{})

def frontend_test(request):
    context = {}
    return render(request, "index.html", context)

### REST CALLS
#-- Post --#
@api_view(['GET', 'POST'])
def neighbourhoods_list(request):
    if request.method == 'GET':
        data = Neighbourhood.objects.all()
        serializer = NeighbourhoodSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NeighbourhoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

## TODO neighbourhoods_details