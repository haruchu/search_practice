from django.shortcuts import render
from .models import People
from django.views.generic import ListView
 
 
class PeopleList(ListView):
    model = People
