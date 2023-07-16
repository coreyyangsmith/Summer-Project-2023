from django.contrib import admin
from .models import User
from .models import Neighbourhood
from .models import Voting

# Register your models here.
admin.site.register(User)
admin.site.register(Neighbourhood)
admin.site.register(Voting)
