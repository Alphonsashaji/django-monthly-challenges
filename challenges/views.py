from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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
    "december":None
}

def index(request):
    list_items=""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html",{
        "months":months
        
    })


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
        return render(request,"challenges/challenge.html", {"text":challenge_text,
        "month_name": month})
     
    except:
        raise Http404()
    