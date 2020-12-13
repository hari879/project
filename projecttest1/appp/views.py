from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render#, render_to_response
from django.contrib import messages
#from django.http import HttpResponseRedirect
from .forms import Companyforms,MaterialForm,NotificationForm
from .models import Material, StudentDetails,Company,Notification
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'home.html',{
        'count':count
    })
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            username= request.POST.get('username')
            password= request.POST.get('password')

            user =  authenticate(request, username=username , password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
             
        return render(request, 'registration/login.html' , {
    }) 


def logoutUser(request):
    logout(request)
    return redirect('home')



def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST) 
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created...!')
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'registration/signup.html' , {
        'form': form
    }) 
@login_required(login_url='login')
def companySignup(request):
    if request.method == 'POST':
        form = Companyforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CompanyList')
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
@login_required(login_url='login')
def profile(request):
    de=StudentDetails()
    de.StudentName="acharya"
    de.studentId= 1245
    return render(request , 'profile.html')
@login_required(login_url='login')
def CompanyData(request,name):
    companyd=Company.objects.get(Company_name=name)
    return render(request, 'CompanyData.html', {
        'companyd' : companyd
    })
@login_required(login_url='login')
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
@login_required(login_url='login')
def materials_list(request):
    materials = Material.objects.all()
    return render(request, 'materials_list.html', {
        'materials' : materials
    })
@login_required(login_url='login')
def CompanyList(request):
    liste = Company.objects.all()
    return render(request, 'CompanyList.html', {
        'liste' : liste
    })
@login_required(login_url='login')
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

@login_required(login_url='login')
def notify(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:        
        form = NotificationForm()
    return render(request, 'notify.html' , {
        'form': form
    })

def show_notification(request, id):
    n = Notification.objects.get(id=id)
    return render(request, 'notification.html',{'notification' : n})

def delete_notification(request, id):
    n = Notification.objects.get(id=id)
    n.viewed = True
    n.save()

    return HttpResponseRedirect('/loggedin')

def loggedin(request):
    n=Notification.objects.filter(viewed=False)
    return render(request, 'loggedin.html', {'fullname':request.user.username, 'notifications' : n})



    

