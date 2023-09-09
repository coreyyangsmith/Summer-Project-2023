import django
from scripts.seeding import load_votes, load_threads, load_posts

'''
Main Seeding Script

Required Files:
scripts/load_vote.py

Output:
Populate local database with saved and random (testing) dataset.
'''

django.setup()

def run():
    load_votes.run()
    load_threads.run()
    load_posts.run()
