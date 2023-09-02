from django.shortcuts import render
from .models import User, Vote, Neighbourhood

from django.utils import timezone

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