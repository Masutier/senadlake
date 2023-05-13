from django.contrib import messages
from django.shortcuts import render, redirect
from raiting.models import Raiting


def home (request):
    ratings = Raiting.objects.all()

    context={"title":"Sena DataLake", "banner":"SENA DataLake", 'ratings':ratings}
    return render(request, 'senadlake/home.html', context)


def project (request):

    context={"title": "Plan"}
    return render(request, 'senadlake/project.html', context)


def privacy (request):

    context={"title": "Privacidad"}
    return render(request, 'senadlake/privacy.html', context)


def page501 (request):

    context={"title": "Privacidad"}
    return render(request, 'senadlake/errors/501.html', context)
