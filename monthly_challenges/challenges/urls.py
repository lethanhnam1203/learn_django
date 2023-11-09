from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index_jan),
    # path("february", views.index_feb),
    path("", views.index),
    path("<month>", views.monthly_challenge_by_number),	
]

