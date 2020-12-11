from django.shortcuts import render
from .models import login_Details
from django.contrib import messages
# Create your views here.

        
def login(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password') :
            saverecord=login_Details()
            saverecord.email=request.POST.get('email')
            saverecord.password=request.POST.get('password')
            saverecord.save()
            messages.success(request,'succesfull..!')
            return render(request,'login.html')
    else:
            return render(request,'login.html')