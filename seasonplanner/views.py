#Create your views here.

from datetime import date, timedelta

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate


from seasonplanner.models import Season, Week
from seasonplanner.forms import SeasonForm

def index(request):
    return HttpResponse("Hello, world. You're at the seasonplanner index page.")

def seasons(request):
    season_list = Season.objects.all().order_by('-start_date')
    context = {'season_list': season_list}
    return render(request, 'seasonplanner/seasons.html', context)

def detail(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    return render(request,'seasonplanner/detail.html', context)
    
def create(request):
    #d = date.today()
    #context = {'today': d.strftime("%Y-%m-%d")}
    #return render(request,'seasonplanner/create.html', context)
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
            for i in [range(form.cleaned_data['length'])]:
                new_week = Week()
                new_week.name = 'Week ' + str(i)
                new_week.start_date = d
                new_week.save()
                d = d + timedelta(day=7)
            
            return HttpResponseRedirect(reverse('seasonplanner:detail', args=(new_season.id,)))
    else:
        form= SeasonForm() # an unbound form

    return render(request,'seasonplanner/create.html', {'form': form, })
