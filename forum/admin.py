from django.contrib import admin

from forum.models import Category, Thread, Post


# Register your models here.
admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Post)