from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("This january works")


def febuary(requests):
    return HttpResponse("Walk for 20mins every day")
