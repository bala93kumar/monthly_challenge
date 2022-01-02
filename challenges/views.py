from django.http.response import HttpResponseBadRequest
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# def january(request):
#     return HttpResponse("This january works")


# def febuary(requests):
#     return HttpResponse("Walk for 20mins every day")


monthly_challenges = {

    'january': "walk every day for 3kms",
    "febuary": "try to be a vegan",
    "march": "learn django",
    "april": "try to meditate",
    "may": "spend more time with family",
    "june": "daily commit your code",
    "july": "solve data structure problems",
    "august": "start learning front end",
    "september": "try to come up with new applications",
    "october": "participate in more meet ups",
    "november": "try applying for jobs in sof",
    "december": "set up new goals"

}


def index(requests):
    listItems = ""
    for i in list(monthly_challenges.keys()):
        redirect_link = reverse("month-challenge", args=[i])
        listItems += f"<li><a href={redirect_link}>{i}</a></li>"

    response = f"<ul>{listItems}</ul>"

    return HttpResponse(response)


def monthly_chlng_by_number(request, month):

    months = list(monthly_challenges.keys())

    if month > (len(months)):
        return HttpResponseNotFound("Invalid month")

    return_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[return_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(requests, month):

    try:
        challenge_text = monthly_challenges[month]
        reponse_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(reponse_data)
    except:
        return HttpResponseNotFound("this month is not in the list")
