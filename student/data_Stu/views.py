from django.shortcuts import render
from .models import student
# Create your views here.
def profile(request):
    all_members = student.objects.all
    return render(request,'profile.html',{'all':all_members})
