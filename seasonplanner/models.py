from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Season(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    def __str__(self):
        return self.name
    def number_of_weeks(self):
        return 52

class Goal(models.Model):
    "Parent Class for defining goals at a variety of levels"
    text = models.CharField(max_length=200)
    completed = models.BooleanField()

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
    season = models.ForeignKey(Season)
    start_date = models.DateField()
    description = models.CharField(max_length=100)
    def __str__(self):
        # How can I update this to calculate the end date by adding 7 to the start date
        return  self.start_date + ' - ' + self.description

#    physical_attributes = models.ManyToManyField(PhysicalAttribute, verbose_name="list of attributes")
            
#class Workout (models.Model):
#    week = models.ForeignKey(Week)
#    workout_date = models.DateField()
#    workout_length = models.IntegerField("Workout Length (minutes)")
#    notes = models.TextField()


    
    
