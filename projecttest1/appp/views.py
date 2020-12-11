from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import Companyforms,MaterialForm
from .models import Material, StudentDetails,Company

# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'home.html',{
        'count':count
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:        
        form = UserCreationForm()
    return render(request, 'registration/signup.html' , {
        'form': form
    }) 

def companySignup(request):
    if request.method == 'POST':
        form = Companyforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:        
        form = Companyforms()
    return render(request, 'registration/CopmanySignupform.html' , {
        'form': form
    })  

'''
def signup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:        
        form = StudentForm()
    return render(request, 'registration/signup.html' , {
        'form': form
    })   ''' 

def mamul(request):
    return render(request, 'mamul.html')

def LoginPage(request):
    return render(request, 'LoginPage.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    de=StudentDetails()
    de.StudentName="acharya"
    de.studentId= 1245
    return render(request , 'profile.html')

def CompanyData(request,name):
    companyd=Company.objects.get(Company_name=name)
    return render(request, 'CompanyData.html', {
        'companyd' : companyd
    })

def upload(request):
    context = {}
    if request.method=='POST':
        uploaded_file=request.FILES['myfile']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        url=fs.url(name)
        context['url'] = fs.url(name)
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'upload.html')   

def materials_list(request):
    materials = Material.objects.all()
    return render(request, 'materials_list.html', {
        'materials' : materials
    })

def CompanyList(request):
    liste = Company.objects.all()
    return render(request, 'CompanyList.html', {
        'liste' : liste
    })

def upload_materials(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('materials')
    else:
        form = MaterialForm()        
    return render(request, 'upload_materials.html', {
        'form': form
        })


