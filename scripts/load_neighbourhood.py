# batch script to populate Neighbourhood based on imported .csv data

import csv
from main.models import Neighbourhood

from django.utils import timezone

DATA_PATH = "scripts/seeding_data/neighbourhood.csv"

def run():
    with open(DATA_PATH) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Neighbourhood.objects.get_or_create(
                code=row[0],
                name=row[1],
                image=row[2],
                sector=row[3],
                created_at=timezone.now(),
                updated_at=timezone.now(),
            )       
    








  