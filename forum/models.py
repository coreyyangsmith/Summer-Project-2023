from django.db import models
from main.models import User, Community

class Category(models.Model):   
    name = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Thread(models.Model):
    name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) #TODO Corey | Add owned rows for Thread

    def __str__(self):
        return self.category.name + "-" + self.name    

class Post(models.Model):
    content = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) #TODO Corey | Add owned rows for Post

    def __str__(self):
        return self.thread.name + "-" + self.content    
