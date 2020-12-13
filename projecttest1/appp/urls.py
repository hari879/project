from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views
'''
urlpatterns = patterns('notification.views',
url(r'^show/?P<notification_id>\d+)/$' , 'show_notification'),
url(r'^delete/?P<notification_id>\d+)/$' , 'delete_notification'),'''

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('accounts/login/',views.loginPage,name='login'),
    path('accounts/logout/',views.logoutUser,name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('notification/',views.notification,name='notification'),
    path('loggedin/',views.loggedin,name='loggedin'),
    path('show/<int:id>/',views.show_notification,name='show'),
    path('delete/<int:id>/',views.delete_notification,name='delete'),
    path('notify',views.notify,name='notify'),
    path('mamul',views.mamul,name='mamul'),
   # path('LoginPage', views.LoginPage,name='LoginPage'),
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