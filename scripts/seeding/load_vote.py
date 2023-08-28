# Script to populate Vote model based based on randomly generated data.
from main.models import Vote, Neighbourhood
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
        random_neighbourhood =  Neighbourhood.objects.order_by("?").first()

        _, created = Vote.objects.get_or_create(
            
            neighbourhood_key= random_neighbourhood,
            vote_time=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
    








  