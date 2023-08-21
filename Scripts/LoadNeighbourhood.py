import csv
from main.models import Neighbourhood

DATA_PATH = "Data/neighbourhood.csv"

# batch script to populate Neighbourhood based on imported .csv data
def run():


    with open(DATA_PATH) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Neighbourhood.objects.get_or_create(
                code=row[0],
                name=row[1],
                image=row[2],
                sector=row[3],
                created_at=row[4],
                updated_at=row[5],
            )           








  