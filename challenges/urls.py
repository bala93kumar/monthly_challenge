
from django.urls import path

from . import views

urlpatterns = [

    # path("january", views.january),
    # path("febuary", views.febuary),
    path("", views.index),
    path("<int:month>", views.monthly_chlng_by_number),
    path("<str:month>", views.monthly_challenge, name='month-challenge'),




]
