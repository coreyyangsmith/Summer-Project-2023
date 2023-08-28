import django
from scripts.seeding import load_neighbourhood, load_vote
from main.models import Neighbourhood, Vote

'''
Main Seeding Script

Required Files:
scripts/load_neighbourhood.py
scripts/load_vote.py

Output:
Populate local database with saved and random (testing) dataset.
'''

django.setup()

def run():
    # Step 1: Delete All Existing Data
    Neighbourhood.objects.all().delete()
    Vote.objects.all().delete()
    # TODO Corey | Metric.objects.all().delete()
    # TODO Corey | Question.objects.all().delete()
    # TODO Corey | Quiz.objects.all().delete()            

    # Step 2: Load Data
    load_neighbourhood.run()
    load_vote.run()
