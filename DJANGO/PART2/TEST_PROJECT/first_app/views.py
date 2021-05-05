from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord  # MTV model


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')  # orderby is like sql 
    date_dict = {'access_records':webpages_list}
    
    return render(request,'first_app/index.html',context=date_dict)

# Steps 1 and 2 of Model Template View completed
