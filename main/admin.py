from django.contrib import admin
from .models import Community, Metric, Question, Quiz, Vote

# Register your models here.
admin.site.register(Community)
admin.site.register(Vote)

admin.site.register(Metric)
admin.site.register(Question)
admin.site.register(Quiz)
