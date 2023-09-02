import django
from scripts.seeding import load_neighbourhoods, load_categories

'''
Initialize DB with Necessary Data

Required Files:
scripts/load_neighbourhood.py

Output:
Populate local database with necessary data.
'''

django.setup()

def run():
    load_neighbourhoods.run()
    load_categories.run()

