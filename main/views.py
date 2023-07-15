from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(response, id):
    user = User.objects.get(id=id)
    return render(response, 'main/display.html', {"user":user})

def home(response):
    return render(response, 'main/home.html',{})