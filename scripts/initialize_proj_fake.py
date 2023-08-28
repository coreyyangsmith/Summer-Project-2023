import django
from scripts.db import clear_db, initialize_db, seed_db

'''
initialize_proj_blank.py

Required Files:
scripts/db/clear_db.py
scripts/db/initialize_db.py
scripts/db/seed_db.py

Output:
Initialize project with necessary data to run webapp, including fake data for testing
'''

django.setup()

def run():
    clear_db.run()
    initialize_db.run()
    seed_db.run()
