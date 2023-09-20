import django
from scripts.seeding import load_communities, load_categories, load_users

'''
Initialize DB with Necessary Data

Required Files:
scripts/load_neighbourhood.py

Output:
Populate local database with necessary data.
'''

django.setup()

def run():
    load_communities.run()
    load_categories.run()
    load_users.run()

