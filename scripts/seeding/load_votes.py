# Script to populate Vote model based based on randomly generated data.
from main.models import Vote, Community
from django.utils import timezone
from scripts.seeding import seeding_options

'''
Seeder Function to load Vote model

Required Files:
None

Output:
Populate local database with random (testing) dataset.
'''

def run():
    for x in range(seeding_options.NUMBER_TO_GENERATE):
        random_community =  Community.objects.order_by("?").first()

        _, created = Vote.objects.get_or_create(
            
            neighbourhood_key= random_community,
            vote_time=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
    print("'Vote' loaded successfully.")    









  