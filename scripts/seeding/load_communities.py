# Script to batch import and populate Neighbourhood model based on imported .csv data
import csv
from main.models import Community
from django.utils import timezone

'''
Seeder Function to load Neighbourhood model

Required Files:
scripts/seeding/seeding_data/neighbourhood.csv

Output:
Populate local database with saved (testing) dataset.
'''

DATA_PATH = "scripts/seeding/seeding_data/community.csv"

def run():
    with open(DATA_PATH) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Community.objects.get_or_create(
                code=row[0],
                name=row[1],
                image=row[2],
                sector=row[3],
                created_at=timezone.now(),
                updated_at=timezone.now(),
            )       
    print("'Community' loaded successfully.")            
    








  