import django
from main.models import Community, Vote

'''
Clear Database

Required Files:
None

Output:
Will completely wipe the local database
'''

django.setup()

def run():
    # Step 1: Delete All Existing Data
    Community.objects.all().delete()
    Vote.objects.all().delete()
    # TODO Corey | Metric.objects.all().delete()
    # TODO Corey | Question.objects.all().delete()
    # TODO Corey | Quiz.objects.all().delete()  

