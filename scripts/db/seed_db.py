import django
from scripts.seeding import load_vote

'''
Main Seeding Script

Required Files:
scripts/load_vote.py

Output:
Populate local database with saved and random (testing) dataset.
'''

django.setup()

def run():
    load_vote.run()
