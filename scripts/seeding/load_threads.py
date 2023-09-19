# Script to batch import and populate Thread model based on imported .csv data
import csv
from forum.models import Thread, Category
from main.models import Community
from django.utils import timezone

'''
Seeder Function to load Thread model

Required Files:
scripts/seeding/seeding_data/thread.csv

Output:
Populate local database with saved (testing) dataset.
'''

DATA_PATH = "scripts/seeding/seeding_data/thread.csv"

def run():
    with open(DATA_PATH) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Thread.objects.get_or_create(
                name=row[2],
                created_at=timezone.now(),
                updated_at=timezone.now(),
                category=Category.objects.get(name=row[1], community=Community.objects.get(code=row[0])),
            )       
    print("'Thread' loaded successfully.")





  