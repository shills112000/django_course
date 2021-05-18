from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm


# Login additions

from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() # grabbing user form, saving to database
            user.set_password(user.password)  # sets password as hash
            user.save() # saves to database again with hash password

            profile = profile_form.save(commit=False) # don't save to database yet, as we want to manipulate first
            profile.user = user # sets up 1 to 1 relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save() # saves to database

            registered = True

        else:
            print(user_form.errors,profile.forms.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    

    return render(request,'basic_app/registration.html',
                            {'user_form':user_form,
                             'profile_form':profile_form,
                             'registered':registered})

# Login views

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("account not active")

        else:
            print ("failed login attempt ",username,password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'basic_app/login.html',{})

@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("you are logined in nice!")


