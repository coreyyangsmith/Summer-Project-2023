# Script to batch import and populate Post model based on imported .csv data
import csv
from forum.models import Post, Thread, Category
from main.models import Community
from django.utils import timezone

'''
Seeder Function to load Category model

Required Files:
scripts/seeding/seeding_data/post.csv

Output:
Populate local database with saved (testing) dataset.
'''

DATA_PATH = "scripts/seeding/seeding_data/post.csv"

def run():
    with open(DATA_PATH) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Post.objects.get_or_create(
                content=row[3],
                created_at=timezone.now(),
                updated_at=timezone.now(),
                thread=Thread.objects.get(name=row[2], category=
                    Category.objects.get(name=row[1], neighbourhood=
                        Community.objects.get(code=row[0]))),
            )       
    print("'Post' loaded successfully.")





  