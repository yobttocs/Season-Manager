from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

# Create your models here.

class Season(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    def __str__(self):
        return self.name
    def number_of_weeks(self):
        return self.week_set.count()

class Goal(models.Model):
    """Parent Class for defining goals at a variety of levels"""
    text = models.CharField(max_length=200)
    completed = models.BooleanField()
    def __str__(self):
        return self.text
    
    class Meta:
        abstract = True

class SeasonGoal(Goal):
    season = models.ForeignKey(Season)
    
#class PhysicalAttribute(models.Model):
#    attribute_name = models.CharField(max_length=100)
#    description = models.CharField(max_length=200)
#
#    def __str__(self):
#        return self.attribute_name + " - " + self.description    

class Week(models.Model):
    """Week class defines each week of the training season"""
    season = models.ForeignKey(Season)
    start_date = models.DateField()
    description = models.CharField(max_length=100)
    def weekrange(self):
        d1 = self.start_date
        d2 = d1 + timedelta(days=7)
        return d1.strftime("%m/%d/%Y") + "-" + d2.strftime("%m/%d/%Y")
    def __str__(self):
        return self.description + ": " + self.weekrange()
    def planned_hours(self):
        s = self.plannedworkout_set.aggregate(models.Sum('workout_length'))
        if s['workout_length__sum'] is None:
            s['workout_length__sum'] = 0
        return s['workout_length__sum']
    
    def completed_hours(self):
        s = self.completedworkout_set.aggregate(models.Sum('workout_length'))
        if s['workout_length__sum'] is None:
            s['workout_length__sum'] = 0
        return s['workout_length__sum']
    
#    physical_attributes = models.ManyToManyField(PhysicalAttribute, verbose_name="list of attributes")
            
class Workout (models.Model):
    week = models.ForeignKey(Week)
    workout_date = models.DateField()
    workout_length = models.IntegerField("Workout Length (minutes)")
    notes = models.TextField()
    def __str__(self):
        return self.workout_date.strftime("%m/%d/%Y") + " - " + str(self.workout_length) + " minutes"
    class Meta:
        abstract = True

class CompletedWorkout(Workout):
    """An implementation of the Workout parent class for tracking completed workouts"""

class PlannedWorkout(Workout):
    """An implementation of the Workout parent class for tracking planned workouts"""
    
    
    
