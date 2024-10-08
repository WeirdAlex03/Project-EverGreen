from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# handles request 
def index(request):
    return render(request,'index.html')
def obj1_css(request):
    return render(request, 'eg_app/static/css/styles.css') # this has to be in a different path other than index.html is
def obj1_js(request):
    return render(request,'eg_app/static/js/functions.js') # and so with this one!