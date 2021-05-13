from django.shortcuts import render
#from first_app.models import User
#from django.http import HttpResponse
from first_app.forms import NewUserForm

def index(request): 
    return render(request,'first_app/index.html')

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        # check validation of
        if form.is_valid():
            form.save(commit=True) # save to database
            return index(request)
        else:
            print ('error form invalid')   # if form post is incorrect
    
    return render (request,'first_app/users.html',{'form':form})
