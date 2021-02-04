from django.urls import path

from . import views

urlpatterns = [
    path('contactteam', views.contactteam, name="contactteam"),
]

