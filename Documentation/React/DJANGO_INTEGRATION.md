# This document will provide a brief explanation of the django/react integration.

# Django currently handles the routing, and to integrate a react front-end into our django back-end, we must tell django where to look for files for its routing.

# After installing a react project into our folder "npx create-react-app frontend", we need navigate to our main settings.py and add the following code:

```import os```

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend', 'build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend', 'build', 'static')]```

# After this we can link up our index.html from React in any view/route the normal way we do that in Django.

```
def frontend_test(request):
    context = {}
    return render(request, "index.html", context)
```

# Then we are free to create stuff within React. You can see that the 'build' folder is hooked up to our template directory - this means to 'save' any changes to our project when we run it, we must run our react project first. To do this, we must navigate to our react (frontend) folder and run the build command.

```cd frontend```
```npm run build```

# After this, we should be free to run our server and navigate to a url and the basic react page should show!

```cd ..```
```python manage.py runserver```