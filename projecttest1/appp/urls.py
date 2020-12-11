from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mamul',views.mamul,name='mamul'),
    path('LoginPage', views.LoginPage,name='LoginPage'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('profile',views.profile,name='profile'),
    path('upload',views.upload,name='upload'),
    path('materials',views.materials_list,name='materials'),
    path('materials/upload',views.upload_materials,name='upload_materials'),
    path('company',views.companySignup,name='companySignup'),
    path('CompanyList',views.CompanyList,name='CompanyList'),
    path('CompanyData/<str:name>/',views.CompanyData,name='CompanyData'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)