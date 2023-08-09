# Django Polls Application Walkthrough

Polls Application

[Part 1: Setup and Requests/Responses](#part-1-setup-and-requestsresponses)

[Part 2: Models and Admin](#part-2-models-and-admin)

[Part 3: Views and Templates](#part-3-views-and-templates)

## Part 1: Setup and Requests/Responses
Ref: https://docs.djangoproject.com/en/4.2/intro/tutorial01/

<ins>**Topics Covered**</ins>
* Creating New Project
* Project Hierarchy/File Structure
* Check Development Server
* Run Development Server
* New App Workflow


<ins>**Important Commands**</ins>
* python -m Django —version
* django-admin startproject mysite .
* python manage.py check
* python manage.py startapp app-name


<ins>**Walkthrough**</ins>

**Step 1: Create New Project**
* run "django-admin startproject mysite ." in the terminal
* ensure you are cd in your project directory

**Step 2: Test Check**
* run "python manage.py check" in terminal
* must cd into project folder previously generated

**Step 3: Run Development Server Test**
* run "python manage.py runserver"

**Step 4: Create Polls App**
* run "python manage.py startapp polls"

**Step 5: Create First View**
* navigate to polls/views.py and add the following code block:
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

**Step 6: Create First Route**
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

**Step 7: Wire Route from Main Project to New App**
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
Ref: https://docs.djangoproject.com/en/4.2/intro/tutorial02/

<ins>**Topics Covered**</ins>
* Migrations
* Models
* Django's ORM

<ins>**Important Commands**</ins>
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser


<ins>**Walkthrough**</ins>

**Step 1: Navigate to "mysite.settings.py"**
* discuss database
* * setup/change database setup here
* * mysqlite3 is default, but can change to MySQL, etc
* discuss installed apps
* * add new apps in here to have django automatically configure
* * needed to process (migrate) models from an app into the main django project
* discuss constants/path variables

**Step 2: Create Models**
* navigate to "polls/models.py"
* explain __str__(self) function
* add the following code snippet:
```
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

**Step 3: "Activate" Models**
* link in django installed apps
```
python manage.py makemigrations polls
```
* run "python manage.py makemigrations"
* run "python manage.py migrate"

```
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

**Step 4: DB Interaction in Shell**
* run "python manage.py shell" to activate shell
* press CTRL+D to exit shell mode
* > "from polls.models import Choice, Question"
* > "Question.objects.all()"
* > "from django.utils import timezone"
* > "q = Question(question_text="What's new?", pub_date=timezone.now())"
* > "q.save()"
* > "q.is"
* > "q.question_text"
* > "q.pub_date"
* > "q.question_test = 'What's up?'"
* > "q.save()"
* > "Question.objects.all()

**Step 5: Setting up Admin Panel
* run "python manage.py createsuperuser"
* wire polls app to admin in "polls/admin.py"
```
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

**Step 6: DB Interaction in Admin**
* login and explore!

## Part 3: Views and Templates
Ref: https://docs.djangoproject.com/en/4.2/intro/tutorial03/

<ins>**Topics Covered**</ins>
* Django Views
* Django Templates

<ins>**Important Commands**</ins>
* TBD


<ins>**Walkthrough**</ins>
**Step 1: TBD***


Notes/Tips
Views
- expects an HttpResponse back!
