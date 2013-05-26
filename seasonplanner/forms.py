from datetime import date
from django import forms
from seasonplanner.models import Workout

class SeasonForm(forms.Form):
    name = forms.CharField(label="Season Name", max_length=200)
    start = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label="Start Date", initial= date.today())
    length= forms.IntegerField(widget=forms.TextInput(attrs={'type':'number','min':4,'max':52,'step':1}),label="Number of Weeks")

class WorkoutForm(forms.Form):
    workout_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label="Workout Date") 
    workout_length = forms.IntegerField(widget=forms.TextInput(attrs={'type':'number','step':1}), label="Length")
    notes = forms.CharField(label="Notes")
    status = forms.CharField(label="Status", max_length=10)
