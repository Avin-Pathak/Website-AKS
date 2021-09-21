from .views_api import *  
from django.urls import path

urlpatterns = [
    path('login/' , LoginView),
    path('register/' , RegisterView)
   
  
]

