import django
from scripts import load_neighbourhood
django.setup()

from main.models import Neighbourhood

def run():
    # Step 1: Delete All Existing Data
    Neighbourhood.objects.all().delete()


    # Metric.objects.all().delete()
    # Question.objects.all().delete()
    # Quiz.objects.all().delete()            

    # Step 2: Load Data
    load_neighbourhood.run()

