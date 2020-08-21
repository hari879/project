from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User , auth
from calc.models import login_Details
# Create your views here.
def login(request):
    return render(request,'login.html')

def newPage(request):
    if request.method =='POST':
        email=request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=email,password=password)
        user.save()
        print('createrd')
        return redirect('/')
    else:
        return render(request,'login.html')        

