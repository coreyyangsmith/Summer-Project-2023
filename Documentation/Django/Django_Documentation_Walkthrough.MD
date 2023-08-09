# Django Documentation Walkthrough
### Resource generated for week 5 meeting presentation.

Polls Application Links
[Part 1: Setup & Requests/Responses](#part-1-setup-requests-responses)

### Part 1: Setup & Requests/Responses
https://docs.djangoproject.com/en/4.2/intro/tutorial01/

Topics Covered:
Creating New Project
Project Hierarchy/File Structure
Run Development Server
Initial Setup Workflow
- Initia
Important Commands:
Python manage.py check
Python manage.py startapp app-name
Python -m Django —version
Django-admin startproject mysite .

Step 1: Create New Project
- Run django-admin startproject mysite .

Step 2: Test Check
- Run python manage.py check

Step 3: Run Development Server Test
- Run python manage.py run server

Step 4: Create Polls App
Run python manage,py start app polls

Step 5: Create First View
HttpResponse


Part 2: Models and Admin
https://docs.djangoproject.com/en/4.2/intro/tutorial02/
Python manage.py createsuperuser
Python manage.py make migrations
Python manage.py migrate

Topics Covered:
Migrations
Models
ORM

Part 3: Views and Templates
https://docs.djangoproject.com/en/4.2/intro/tutorial03/

Topics Covered:
HTML


Notes/Tips
Views
- expects an HttpResponse back!
