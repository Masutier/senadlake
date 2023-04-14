import json
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *


@unauthenticated_user
def registerUser(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            group = Group.objects.get(name='user_rol')
            user.groups.add(group)
            login(request, user)
            messages.success(request, f'The User was created successfuly, Now create the rest of the info')
            return redirect("userProfile")
        else:
            messages.error(request, f"Something went wrong. We are sorry")
            return redirect("home")
    else:
        form = UserRegisterForm()

    context = {'title':'User Register', "banner": "User Register", 'form':form}
    return render(request, 'users/registerUser.html', context)


@unauthenticated_user
def loginPage(request):
    form = LogInForm()
    
    if request.method == 'POST':
        form = LogInForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, f'Algo no salio bien, Intentalo de nuevo')
            return redirect('home')

    context = {'title':'LogIn', 'form':form}
    return render(request, 'users/login.html', context)



def userLogout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='loginPage')
def userProfile(request):

    context = {'title':'User Profile', 'banner':"Profile"}
    return render(request, 'users/user_profile.html', context)
