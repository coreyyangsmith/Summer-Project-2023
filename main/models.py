from django.db import models
# from django.contrib.gis.db import models
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
    code = models.CharField(max_length = 3, default="AAA")    
    name = models.CharField(max_length = 40, default="DEFAULT")
    image = models.FilePathField(path="/media/uploads", recursive = True)
    sector = models.CharField(max_length=9, default="DEFAULT")
    # location = models.PointField() # lat long data for neighbourhood geographic 'centre'
    # multipolygon = models.MultiPolygonField() # multipolygon boundary
    created_at = models.DateTimeField(default="Created UTC")
    updated_at = models.DateTimeField(default="Updated UTC")

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
    name = models.CharField(max_length=20)
    neighourhood_key = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)
    actual_value = models.FloatField()
    actual_wgt = models.FloatField()
    perceived_value = models.FloatField()
    perceived_wgt = models.FloatField()
    created_at = models.DateTimeField(default="Created UTC")
    updated_at = models.DateTimeField(default="Updated UTC")

class Quiz(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    score = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(default="Created UTC")
    updated_at = models.DateTimeField(default="Updated UTC")

class Question(models.Model):
    name = models.CharField(max_length=20)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE) 
    comparison = models.CharField(max_length=16) # greaterthan, lessthan, greaterthanequal, lessthanequal, notequal, equal
    metric_id_1 = models.ForeignKey(Metric, on_delete=models.CASCADE) # grab metric ID to then grab neighbourhood ID for comparison
    metric_id_2 = models.ForeignKey(Metric, on_delete=models.CASCADE) # grab metric ID to then grab neighbourhood ID for comparison
    created_at = models.DateTimeField(default="Created UTC")
    updated_at = models.DateTimeField(default="Updated UTC")

## Many-to-Many Model Relationship Implementation
# 
class QuestionSet(models.Model):
    name = models.CharField(max_length=20)