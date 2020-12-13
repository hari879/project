from django import forms
#from django.contrib.auth.forms import UserCreationForm
from .models import *


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('FileName','pdf')

class Companyforms(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__' 

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('title','message')