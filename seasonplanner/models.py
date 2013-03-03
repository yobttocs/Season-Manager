from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Season(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    start_date = models.DateField()

class Goal(models.Model):
    "Parent Class for defining goals at a variety of levels"
    text = models.CharField(max_length=200)
    completed = models.BooleanField()

    class Meta:
        abstract = True

class SeasonGoal(Goal):
    season = models.ForeignKey(Season)

class PhysicalAttribute(models.Model):
    attribute_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.attribute_name + " - " + self.description    

class Week(models.Model):
    season = models.ForeignKey(Season)
    description = models.CharField(max_length=100)
    physical_attributes = models.ManyToManyField(PhysicalAttribute, verbose_name="list of attributes")    
     
class Workout (models.Model):
    week = models.ForeignKey(Week)
    workout_date = models.DateField()
    workout_length = models.IntegerField("Workout Length (minutes)")
    notes = models.TextField()


    
    
