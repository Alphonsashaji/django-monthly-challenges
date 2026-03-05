from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges={
    "january":"Study Django for 2 hours daily!",
    "february":"Work on project features for 2 hour daily!",
    "march":"Practice coding problems for 30 minutes daily!",
    "april":"Revise Python concepts regularly!",
    "may":"Walk for 20 minutes daily!",
    "june":"Maintain consistency in learning and development!",
    "july":"Explore new Django concepts every week!",
    "august":"Push code updates to GitHub weekly!",
    "september":"Improve UI/UX of the project gradually!",
    "october":"Read tech blogs or documentation weekly!",
    "november":"Practice SQL queries daily!",
    "december":"Take short breaks to avoid burnout!"
}

def index(request):
    list_items=""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month= month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

     
    response_data=f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months= list(monthly_challenges.keys())
 
    if month> len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month= months[month - 1]
    redirect_path= reverse("month-challenge", args=[redirect_month] )  # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text= monthly_challenges[month]
        response_data=f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    