from django.contrib import admin
from django.urls import path
from basic_app import views
from django.conf.urls import url

# TEMPLDATE URLSearchParams
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.user_login,name='user_login'),
    path('special/', views.special,name='special')
]