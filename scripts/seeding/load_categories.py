# Script to batch import and populate Category model based on imported .csv data
import csv
from forum.models import Category
from main.models import Neighbourhood
from django.utils import timezone

'''
Seeder Function to load Category model

Required Files:
scripts/seeding/seeding_data/category.csv

Output:
Populate local database with saved (testing) dataset.
'''

DATA_PATH = "scripts/seeding/seeding_data/category.csv"

def run():
    with open(DATA_PATH) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Category.objects.get_or_create(
                name=row[1],
                created_at=timezone.now(),
                updated_at=timezone.now(),
                neighbourhood=Neighbourhood.objects.get(code=row[0]),
            )       
    print("'Category' loaded successfully.")





  