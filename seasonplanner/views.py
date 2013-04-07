# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import date

from seasonplanner.models import Season

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
    d = date.today()
    context = {'today': d.strftime("%Y-%m-%d")}
    return render(request,'seasonplanner/create.html', context)


