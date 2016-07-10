from django.shortcuts import render
from django.http import HttpResponse

from .models import Show, Stage, Venue

# Create your views here.
def index(request):
    return HttpResponse("You're at the shows index")

def stage_index(request):
    return HttpResponse("You're at the stages index")

def venue_index(request):
    return HttpResponse("You're at the venues index")    

def show_detail(request, show_id):
    return HttpResponse("You're looking at show %s." % show_id)

def stage_detail(request, stage_id):
    return HttpResponse("You're looking at stage %s." % stage_id)

def venue_detail(reqeust, venue_id):
    return HttpResponse("You're looking at venue %s.", venue_id)