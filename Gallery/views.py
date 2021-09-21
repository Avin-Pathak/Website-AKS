from django.shortcuts import render
from .models import *

# Create your views here.

def see_photo(request):
    context = {'photos' : PhotoModel.objects.all}
    return render(request , 'see_photo.html', context)
