import django
from scripts.db import clear_db, initialize_db

'''
initialize_proj_blank.py

Required Files:
scripts/db/clear_db.py
scripts/db/initialize_db.py

Output:
Initialize project with necessary data to run webapp
'''

django.setup()

def run():
    clear_db.run()
    initialize_db.run()
