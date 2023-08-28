import django
from scripts.seeding import load_neighbourhood, load_vote
from main.models import Neighbourhood, Vote

'''
Clear Database

Required Files:
None

Output:
Will completely wipe the local database
'''

def run():
    # Step 1: Delete All Existing Data
    Neighbourhood.objects.all().delete()
    Vote.objects.all().delete()
    # TODO Corey | Metric.objects.all().delete()
    # TODO Corey | Question.objects.all().delete()
    # TODO Corey | Quiz.objects.all().delete()  

