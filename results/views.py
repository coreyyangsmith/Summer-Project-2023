from django.shortcuts import render
from django.http import HttpResponse

# test data for results page and linked Javascript file (delete after)
TEST_DATA = ["ABB.jpg", "BRI.png", "CIT.png", "DNE.jpg", "FLN.jpg", "KIN.png", "MIS.jpg", "PCK.jpg", "RIV.png", "SHS.png",   "TEM.png"]

data = {"test": TEST_DATA}

def index(response):
    return render(response, 'results/results.html', data)