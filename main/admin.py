from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)
admin.site.register(Neighbourhood)
admin.site.register(Voting)
