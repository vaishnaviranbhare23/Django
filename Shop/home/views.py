from django.shortcuts import render, HttpResponse


def index(request):
    context = {}
    return render(request, 'base.html')


def about(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'services.html')


def services(request):
    return render(request, 'services.html')

# Create your views here.
