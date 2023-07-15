from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 62)
    num_votes = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name