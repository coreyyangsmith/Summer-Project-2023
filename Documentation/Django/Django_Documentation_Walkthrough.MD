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
```
> python -m Django —version
> django-admin startproject mysite .
> python manage.py check
> python manage.py startapp app-name
```

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
```
> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
```

<ins>**Walkthrough**</ins>

**Step 1: Navigate to "mysite.settings.py"**
* discuss database
* * setup/change database setup here
* * mysqlite3 is default, but can change to MySQL, etc
* discuss installed apps
* * add new apps in here to have django automatically configure
* * needed to process (migrate) models from an app into the main django project
* * also need to add extensions here
* discuss constants/path variables

**Step 2: Create Models**
* [Link to Django Docs - Model Field References](https://docs.djangoproject.com/en/4.2/ref/models/fields/)
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
* link in django installed apps in "mysite/settings.py"
```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "polls.apps.PollsConfig",
]
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
```
> from polls.models import Choice, Question
> Question.objects.all()
> from django.utils import timezone
> q = Question(question_text="What's new?", pub_date=timezone.now())
> q.save()
> q.is
> q.question_text
> q.pub_date
> q.question_test = 'What's up?'
> q.save()
> Question.objects.all()
```

**Step 5: Setting up Admin Panel
* run "python manage.py createsuperuser"
* wire polls app to admin in "polls/admin.py"
```
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

**Step 6: DB Interaction in Admin**
* run server
* navigate to "domain/admin"
* login and explore

## Part 3: Views and Templates
Ref: https://docs.djangoproject.com/en/4.2/intro/tutorial03/

<ins>**Topics Covered**</ins>
* Django Views
* Django Templates

<ins>**Important Commands**</ins>
* TBD


<ins>**Walkthrough**</ins>
**Step 1: Create Additional Views**
* navigate to "polls/views.py"
* add the following code block:
```
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

**Step 2: Route in URLs**
* navigate to "polls/urls.py"
* add the following code block:
```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
* check and runserver test

**Step 3: Views and Data**
* add the following code block:
```
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```

**Step 4: Create Templates Folder**
* templates are gloabal
* due to namespace and django's internal, we must specify a funky file path
* create "polls/templates" subfolder
* create "polls/templates/polls" subfolder
* create html document in "polls/templates/polls"
* add the following code block:
```
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

**Step 5: Django Templating Language**
* [Link to Django Docs - Django Templating Language](https://docs.djangoproject.com/en/4.2/ref/templates/language/)
* can access DTL and create functional code blocks using single curly braces {}
* can access variables using double curly braces
* can slot in components and extend other html "extends"
* can write conditionals, loops, use variables, etc
```
{% for k, v in defaultdict.items %}
    Do something with k and v here...
{% endfor %}
```

**Step 6: Adjust View to Render Template**
* views expect HTTPResponse to send back to the URL, as discussed in request/response cycle
* we can render a view and pass in  a 'context' (variables, other relevant info used to generate page)
```
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

* a django shortcut to write this:
```
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

**Step 7: Error Handling**
* we can use the same try/except/raise code to handle errors as with normal python
* as we are dealing with webservers, there are different standards for error codes
* [Link to Wikipedia - HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* refactor detail view:
```
from django.http import Http404
from django.shortcuts import render

from .models import Question

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```
* of course, django has a more consise way of handling this:
```
from django.shortcuts import get_object_or_404, render

from .models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

**Step 8: Create Detail Template**
* generate detail.html in "polls/templates/polls/"
```
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

**Step 9: Hardcoded vs Relative URLs**
* nagivate back to "polls/templates/polls/index.html"
* we can use a shortcut for the url definition - and specify a 'function call' name of sorts in our view as well (more like a url call reference)
```
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```
```
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

**Step 10: Add Namespace to URLs**
* convention to add app_name = "app-name"
* if there are multiple urls that have the same path, this will allow you reference them independently
```
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
* if we specify the namespace in the views, we must also reference in any url references:
```
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```
