from django.db import models
import timezone
from django.utils import timezone

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 62)
    num_votes = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Neighbourhood(models.Model):
    neighbourhood_key = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 40)
    code = models.CharField(max_length = 3)
    image = models.FilePathField(path="/media/uploads", recursive = True)

    def __str__(self):
        return self.name

class Voting(models.Model):
    vote_key = models.IntegerField(primary_key = True)
    neighbourhood_key = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)
    user_info = models.CharField(max_length = 200) # placeholder
    vote_time = models.DateTimeField("Timestamp when user submitted")

    def __str__(self):
        return self.user_info

    def timestamp(self):
        return self.vote_time >= timezone.now() - datetime.timedelta(days=1)