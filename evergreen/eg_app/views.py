from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import util.validators as val

# handles request 
def index(request):
    return render(request,'index.html')

def password_valid_view(request):
    if request.method == "POST":
        password = request.POST.get("password")
        # this uses the method from Alex's Method
        isValid = val.validate_password(password)

        return JsonResponse({"valid_pass":isValid})





