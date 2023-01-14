from django.contrib import admin
from django.urls import path
from .views import (index, services, contact, about)

urlpatterns = [

    path('', index, name="index"),
    path('/services', services, name="services"),
    path('/contact', contact, name="contact"),
    path('/about', about, name="about")
]
