# batch script to populate X based on imported .csv
import csv
from main.models import Metric

DATA_PATH = "Data/metric.csv"

#WIP 

with open(DATA_PATH) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Metric.objects.get_or_create(
            name=row[0],
            neighourhood_key=row[1],
            actual_value=row[2],
            actual_wgt=row[3],
            perceived_value=row[4],
            perceived_wgt=row[5],
            created_at=row[6],
            updated_at=row[7],
        )