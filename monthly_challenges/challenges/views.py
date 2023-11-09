from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):	
    return HttpResponse("Hello World!")

# def index_jan(request):	
#     return HttpResponse("T muon co nhat nhieu tien")

# def index_feb(request):	
#     return HttpResponse("T muon mua nha va o to")

def monthly_challenge_by_number(request, month):
    if month == 'january':
        challenge_text = "Eat no meat for the entire month"
    elif month == 'february':
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == 'march':
        challenge_text = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)

