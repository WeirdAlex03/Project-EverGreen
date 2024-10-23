from django.shortcuts import render

import eg_app.eg_util.validators as val

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# handles request 
def index(request):
    return render(request,'index.html')

@csrf_exempt
def validate_pass(request):
    if request.method == "POST":
        password = request.POST.get("password")
        # this uses the method from Alex's Method
        isValid = val.validate_password(password)
        print(isValid)
        return JsonResponse({"valid_pass":str(isValid)})



