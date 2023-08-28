# Script to batch import and populate Metric model based on imported .csv
import csv
from main.models import Metric

'''
Seeder Function to load Metric model

Required Files:
scripts/seeding/seeding_data/metric.csv

Output:
Populate local database with saved (testing) dataset.
'''

DATA_PATH = "scripts/seeding/seeding_data/metric.csv"

# FUNCITON IS WIP, NOT FUNCTIONAL
# TODO COREY | CREATE METRIC DATASET TO BE IMPORTED TO METRIC MODEL
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