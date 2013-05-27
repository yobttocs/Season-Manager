#Create your views here.

from datetime import date, timedelta

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.views.generic import DetailView

from seasonplanner.models import Season, Week, SeasonGoal, Workout, CompletedWorkout, PlannedWorkout
from seasonplanner.forms import SeasonForm, WorkoutForm

class SeasonDetail(DetailView):

    model = Season
    template_name = 'seasonplanner/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SeasonDetail, self).get_context_data(**kwargs)
        # Add a Queryset of associated weeks
        context['week_list'] = Week.objects.filter(season=context['season'])
        context['goal_list'] = SeasonGoal.objects.filter(season=context['season'])
        return context

def index(request):
    return HttpResponse("Hello, world. You're at the seasonplanner index page.")

def seasons(request):
    season_list = Season.objects.all().order_by('-start_date')
    context = {'season_list': season_list}
    return render(request, 'seasonplanner/seasons.html', context)

def detail(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    return render(request,'seasonplanner/detail.html', {})
    
def create(request):
    """ Create a new season and the selected number of weeks """
    if request.method == 'POST':
        #Bind the form to the data from the request
        form = SeasonForm(request.POST)
        if form.is_valid(): #All rules have passed
            #Process the request
            new_season = Season()
            # For now this code automatically sets the owner of all Seasons to me
            u = authenticate(username='test', password='test123')
            new_season.owner = u
            new_season.name = form.cleaned_data['name']
            new_season.start_date = form.cleaned_data['start']
            new_season.save()
            d = new_season.start_date
            for i in range(form.cleaned_data['length']):
                new_week = Week()
                new_week.season = new_season
                new_week.description = 'Week ' + str(i+1)
                new_week.start_date = d
                new_week.save()
                d = d + timedelta(days=7)
            
            return HttpResponseRedirect(reverse('seasonplanner:detail', args=(new_season.id,)))
    else:
        form= SeasonForm() # an unbound form

    return render(request,'seasonplanner/create.html', {'form': form, })

class WeekDetailView(DetailView):
    model = Week
    template_name = 'seasonplanner/week_detail.html'

def workout_create(request):
    """
    Create a new Workout (either planned or completed) associated with a
    given week
    """
    if request.method == 'POST':
        #Bind the form to the data from the request
        form = WorkoutForm(request.POST)
        if form.is_valid(): # All rules have passed
            # Process the request
            if form.cleaned_data['status'] == 'COMPLETED':
                w = CompletedWorkout()
            else:
                w = PlannedWorkout()
            w.week = Week.objects.get(description = 'Week 1')
            w.workout_date = form.cleaned_data['workout_date']
            w.workout_length = form.cleaned_data['workout_length']
            w.notes = form.cleaned_data['notes']
            w.save()
            
        return HttpResponseRedirect(reverse('seasonplanner:week_detail', args=(w.week.id,)))

    else:
        form = WorkoutForm() # an unbound form

    return render(request, 'seasonplanner/workout_create.html', {'form': form, })
