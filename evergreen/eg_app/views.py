from django.shortcuts import render

# Create your views here.

# handles request 
def index(request):
    return render(request,'index.html')



