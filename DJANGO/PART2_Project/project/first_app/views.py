from django.shortcuts import render
from first_app.models import User

# Create your views here.
from django.http import HttpResponse

def index(request):
    user_list = User.objects.order_by('last_name')  # orderby is like sql 
    user_dict = {'user_data':user_list}
    
    return render(request,'first_app/index.html',context=user_dict)