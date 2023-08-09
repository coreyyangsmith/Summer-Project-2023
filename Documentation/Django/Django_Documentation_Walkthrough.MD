# Django Documentation Walkthrough
### Resource generated for week 5 meeting presentation.

Polls Application
[Part 1: Setup & Requests/Responses](#part-1-setup-requests-responses)

[Part 2: Models and Admin](#part-2-models-and-admin)

[Part 3: Views and Templates](#part-3-views-and-templates)

### Part 1: Setup & Requests/Responses
https://docs.djangoproject.com/en/4.2/intro/tutorial01/

Topics Covered:
* Creating New Project
* Project Hierarchy/File Structure
* Check Development Server
* Run Development Server
* New App Workflow


Important Commands:
* python -m Django —version
* django-admin startproject mysite .
* python manage.py check
* python manage.py startapp app-name


Step 1: Create New Project
* run "django-admin startproject mysite ." in the terminal
* ensure you are cd in your project directory

Step 2: Test Check
* run "python manage.py check" in terminal
* must cd into project folder previously generated

Step 3: Run Development Server Test
* run "python manage.py runserver"

Step 4: Create Polls App
* run "python manage.py startapp polls"

Step 5: Create First View
* navigate to polls/views.py
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```


### Part 2: Models and Admin
https://docs.djangoproject.com/en/4.2/intro/tutorial02/
Python manage.py createsuperuser
Python manage.py make migrations
Python manage.py migrate

Topics Covered:
Migrations
Models
ORM

### Part 3: Views and Templates
https://docs.djangoproject.com/en/4.2/intro/tutorial03/

Topics Covered:
HTML


Notes/Tips
Views
- expects an HttpResponse back!
