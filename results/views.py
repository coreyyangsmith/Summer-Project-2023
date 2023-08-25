from django.shortcuts import render
from django.http import HttpResponse

# test data for results page and linked Javascript file (delete after)
TEST_DATA = ["ABB", "BRI", "CIT", "DNE", "FLN", "KIN", "MIS", "PCK", "RIV", "SHS"]
test_community_data = {"community_codes": TEST_DATA}

def index(response):
    return render(response, "results/results.html", test_community_data)