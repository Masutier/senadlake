from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def raiting(request):
    if request.method == 'POST':
        form = RaitingForm(request.POST)
        form.message  = request.POST.get('message')
        form.stars  = request.POST.get('stars')
        print(form.stars)

        if form.is_valid():
            pform = form.save(commit=False)
            pform.message  = request.POST.get('message')
            pform.stars  = request.POST.get('stars')
            pform.save()

            messages.success(request, f"Your review was created successfully")
            return redirect("home")
        else:
            messages.error(request, f"Something went wrong. We are sorry")
            return redirect("home")
    else:
        form = RaitingForm()

    context={"title":"Raiting", "banner":"Raiting Testing", "form":form}
    return render(request, 'raiting/raiting.html', context)


def testing(request):
    ratings = Raiting.objects.all()

    context={"title":"Testing", "banner":"Review Testing", 'ratings':ratings}
    return render(request, 'raiting/test.html', context)


# mailing