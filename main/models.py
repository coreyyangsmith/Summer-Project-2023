from django.db import models
from django.contrib.gis.db import models
import datetime
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
    code = models.CharField(max_length = 3)    
    name = models.CharField(max_length = 40)
    image = models.FilePathField(path="/media/uploads", recursive = True)
    sector = models.CharField(max_length=9)
    latitude = models.PointField()
    multipolygon = models.MultiPolygonField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.code + "-" + self.name

class Voting(models.Model):
    vote_key = models.IntegerField(primary_key = True)
    neighbourhood_key = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)
    user_info = models.CharField(max_length = 200) # placeholder
    vote_time = models.DateTimeField("Timestamp when user submitted")

    def __str__(self):
        return self.user_info

    def timestamp(self):
        return self.vote_time >= timezone.now() - datetime.timedelta(days=1)
    
class Metric(models.Model):
    name = models.CharField(20)
    neighourhood_key = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)
    actual_value = models.FloatField()
    actual_wgt = models.FloatField()
    perceived_value = models.FloatField()
    perceived_wgt = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Question(models.Model):
    name = models.CharField(20)

class Quiz(models.Model):
    name = models.CharField(20)