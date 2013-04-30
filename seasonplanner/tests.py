"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from seasonplanner.models import Season, Week
from datetime import date, timedelta
from django.contrib.auth.models import User

def week_generator(season, weeks):
    d = date.today()
    for week in range(weeks):
        w = Week()
        w.season = season
        w.start_date = d
        w.description = 'Week: ' + str(week)
        w.save()
        d = d + timedelta(days=7)

def season_generator():
        s = Season()
        s.owner = User.objects.create_user('test','yobttocs@hotmail.com','test123')
        s.name = 'Test Season'
        s.start_date = date.today()
        s.save()
        return s
        
class SeasonTest(TestCase):
    def test_0_weeks(self):
        """
        Tests that Season.number_of_weeks function returns 0 if no weeks are
        defined
        """
        s = season_generator()
        self.assertEqual(s.number_of_weeks(),0)

    def test_1_week(self):
        """
        Tests that Season.number_of_weeks function returns 1 if a single week is
        defined
        """
        s = season_generator()
        
        week_generator(s, 1)
        self.assertEqual(s.number_of_weeks(),1)

    def test_weeks(self):
        """
        Tests that Season.number_of_weeks function returns the correct value if
        an arbitrary number of weeks are defined
        """
        s = season_generator()
        week_generator(s, 52)
        self.assertEqual(s.number_of_weeks(),52)

class WeekTest(TestCase):
    def test_weekrange(self):
        """
        Tests the weekrange method of the Week class.  It requires start_date
        to be set.
        """
        s = season_generator()
        w = Week(season = s)
        w.start_date = date.today()
        w.save()
        t = date.today().strftime("%m/%d/%Y") + '-' + (date.today() + timedelta(days=7)).strftime("%m/%d/%Y")
        self.assertEqual(w.weekrange(),t)
