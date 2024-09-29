from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# handles request 
def index(request):
    return render(request,'templates/index.html')
