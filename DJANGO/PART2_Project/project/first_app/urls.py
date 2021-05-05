from django.conf.urls import url
from first_app import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('users/',views.index,name='index'),
]
