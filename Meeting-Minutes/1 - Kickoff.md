# ⬇ This Week
_Git Branching, MVC Architecture & Basic Web Architecture_

# 📖 Agenda
1. Introduction (25 mins)
   * Agenda
   * Who Am I
   * [Project Overview](#project-overview)
   * [GitHub Education](https://education.github.com)
   * Git Project Setup, Virtual Envs, Repo Invites
   * [Guidelines](#guidelines)
   * Group Selection

 2. Project Management (45 min)
    * [Agile Development Introduction](#agile-development-pt1)
      * Why Agile?
      * Agile Methodology
      * Agile Meetings
    * [Ticket Overview](#ticket-overview)
      * User Stories
      * Acceptance Criteria
      * Definition of 'Done'
    * [Git Branch/Merge/PR](#git-branch-merge-pr)
    * [First Ticket Walkthrough - Django Hello World](#django-first-ticket-walkthrough)

  3. Lecture (20 min)
     * [MVC Architecture](#mvcmvt-architecture)
     * [Web Architecture](#web-architecture)
     * [Front-End Development Process]()
     * [Back-End Development Process]()
    
  4. Working Session
     * Brainstorm/Define MVP
     * Conceptual Design (CRC Cards)
     * User Stories/Ticket Generation

# 📚 Resources
### Project-Overview
* Front-End: [React](https://gist.github.com/tkrotoff/b1caa4c3a185629299ec234d2314e190)
* Back-End: [Django](https://www.youtube.com/watch?v=S9JcI254DZI&t=186s)
* Database: [MySQL](https://www.youtube.com/watch?v=fWC5tP9hDms)
* Deployment: [Heroku](https://www.heroku.com)
* [Framework vs Library](https://www.freecodecamp.org/news/the-difference-between-a-framework-and-a-library-bd133054023f/)

### Guidelines
1. Work on tickets in new branches and submit a pull request to merge to main.
2. Don't ruin the fun! We are all learning in public, there may be some stumbles along the way.

### Agile-Development-pt1
* [Agile Meetings - Video](https://www.youtube.com/watch?v=VW0Sn_ZKumg)
* [Scrum Introduction & User Stories](https://www.youtube.com/watch?v=9TycLR0TqFA)

### Ticket-Overview
* [User Stories - Video](https://www.youtube.com/watch?v=MQzS30PtsiM)
* [User Stories - Article](https://www.atlassian.com/agile/project-management/user-stories)
* [Acceptance Criteria/Definition of 'Done'](https://www.productplan.com/glossary/acceptance-criteria/#:~:text=In%20Agile%2C%20acceptance%20criteria%20refer,consider%20the%20user%20story%20finished.)

### Git-Branch-Merge-PR
* [Git Branching Introduction - !!!](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
* [Git Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
* [Making A Pull Request](https://www.atlassian.com/git/tutorials/making-a-pull-request)
* [Making A Pull Request - GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
* VCS = Version Control System

### Django-(First-Ticket-Walkthrough)
* [Django Setup & Hello World pt1 - !!!](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
* [Django Setup - Video](https://www.youtube.com/watch?v=HBE4K1Xu9us&t=354s)
* Django Commands (to get started; hello world)
  * django-admin startproject helloworld .
    * initializes django project (. adds to current folder, without it will create new subfolder)
  * python manage.py migrate
    * creates local db
  * python manage.py runserver
    * creates lightweight local server to run app
  * python manage.py startapp polls
    * creates app directory
##### Other Resources
* [Django Documentation](https://docs.djangoproject.com/en/4.2/)
* [Django for Everybody - Free Online Course](https://youtu.be/o0XbHvKxw7Y)
* Django Version = 4.2.2 LTS (pip install Django==4.2.2)
* Python Version = 3.11.3 LTS

### MVC/MVT Architecture
* [What is MVC? - !!!](https://www.interserver.net/tips/kb/mvc-advantages-disadvantages-mvc/)
* [Intro to MVT Architecture](https://data-flair.training/blogs/django-architecture/amp/)
* [Another MVT Resource](https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django-edda05b9f43f)

### Web Architecture
* [Basic Web Design](https://www.edrawsoft.com/website-system-design.html)
* [Web Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)

### Front-End Development Process
* [Front-End High-Level Overview](https://i-verve.com/blog/front-end-design-development)
* [Front-End Development Roadmap](https://roadmap.sh/frontend)

##### Other Resources
* [Figma](https://www.figma.com)
* [Lucidchart](https://www.lucidchart.com/pages/)

### Back-End Development Process
* [Back-End High-Level Overview](https://ddi-dev.com/blog/programming/backend-development-key-languages-technologies-features-in-2020/)
* [Back-End Development Roadmap](https://roadmap.sh/backend)

### Inspiration
* [Learn to Program in 10 Years](https://norvig.com/21-days.html)

# ❓ Questions for Better Understanding
### Agile Development
1. Write an example of a user story for the customer(renter) of a car in a car rental company.
2. What is the purpose and reason of using acceptance criteria?

### Git Branching
1. How does Git store its data, and what does a commit object contain?
2. What is the purpose of the HEAD pointer in Git's branching system?
3. What commands are needed to produce and switch to a new branch?
4. What commands are needed to merge your current branch to the main branch?

### MVC Architecture
1. How does a Template vary from the definition of a View? What is Django's 'opinion' on this?
2. Which layer holds the business logic?
3. Describe the control flow for if a user accesses a form, fills a form, and then submits a form. Describe using MVC architecture.
4. Describe the control flow for if a user accesses a form, fills a form, and then submits a form. Describe using MVT architecture.
5. How is a View different in MVC vs MVT architecture?

### Web Architecture / Django
1. What is the difference between a django app and a django project?

# Homework
* Generate a User Story for some aspect of the MVP.
* Using this User Story, generate a well-documented ticket with a clear "Definition of 'Done'"

# ➡ Next Week
_Creating a Model & Basic Database Operations_

# Lecture Summary
[Presentation Slide Deck](https://docs.google.com/presentation/d/1_gjG6ElZ7lMB6ZUCQbVMFIP8YyGzoeEoH1y50qJ-xY4/edit?usp=sharing)

[Lecture Video Part 1 - Introduction](https://www.youtube.com/watch?v=7e58UV4g5mE)
