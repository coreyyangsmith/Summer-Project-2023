from django.contrib import admin
from .models import User, Neighbourhood, Metric, Question, Quiz, Voting


# Register your models here.
admin.site.register(User)
admin.site.register(Neighbourhood)
admin.site.register(Voting)

admin.site.register(Metric)
admin.site.register(Question)
admin.site.register(Quiz)
