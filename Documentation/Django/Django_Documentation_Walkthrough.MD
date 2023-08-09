# Django Polls Application Walkthrough
##### Resource generated for week 5 meeting presentation.

Polls Application

[Part 1: Setup & Requests/Responses](#part-1-setup---requests-responses)

[Part 2: Models and Admin](#part-2-models-and-admin)

[Part 3: Views and Templates](#part-3-views-and-templates)

## Part 1: Setup & Requests/Responses
https://docs.djangoproject.com/en/4.2/intro/tutorial01/

**Topics Covered**
* Creating New Project
* Project Hierarchy/File Structure
* Check Development Server
* Run Development Server
* New App Workflow


**Important Commands**
* python -m Django —version
* django-admin startproject mysite .
* python manage.py check
* python manage.py startapp app-name


**Walkthrough**

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
* navigate to polls/views.py and add the following code block:
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

Step 6: Create First Route
* also able to call classes/functions within the views.py files
* able to further specify the relative path, that will end up calling certain functions
* navigate to polls/urls.py and add the following code block:
```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

Step 7: Wire Route from Main Project to New App
* 'include' function allows referencing other URLs
* navigate to mysite/urls.py (main project urls file) and add the following code block:
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```


## Part 2: Models and Admin
https://docs.djangoproject.com/en/4.2/intro/tutorial02/
Python manage.py createsuperuser
Python manage.py make migrations
Python manage.py migrate

Topics Covered:
Migrations
Models
ORM

## Part 3: Views and Templates
https://docs.djangoproject.com/en/4.2/intro/tutorial03/

Topics Covered:
HTML


Notes/Tips
Views
- expects an HttpResponse back!
