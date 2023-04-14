
def register(request):
    cities = []
    if request.method == 'POST':
        with open('static/json/us_states_and_cities.json') as statesFile:
            states = json.load(statesFile)

        user_form = UserRegisterForm(request.POST)
        profile_form= ProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            print(user)
            group = Group.objects.get(name='user_rol')
            user.groups.add(group)
            user.save()
            userprofile = profile_form.save(commit=False)
            userprofile.user = user
            num = str(profile_form.cleaned_data.get('phone'))
            if len(num) == 10:
                phoneNum = ("("+num[:3]+")"+num[3:6]+"-"+num[6:])

            userprofile.phone = phoneNum
            userprofile.save()
            messages.success(request, f'The account was created successfuly')
            return redirect('login')
        else:
            messages.error(request, f"Something went wrong. We are sorry")
            return redirect("home")

    else:
        user_form = UserRegisterForm(request.POST, prefix='user')
        profile_form = ProfileForm(request.POST, prefix='userprofile')

        with open('static/json/us_states_and_cities.json') as statesFile:
            states = json.load(statesFile)

            for j in states['Florida']:
                cities.append(j)
            cities.sort()

    context = {'title':'Registro', "banner": "Register", 'user_form':user_form, 'profile_form':profile_form, 'cities':cities}
    return render(request, 'users/registerUser.html', context)
