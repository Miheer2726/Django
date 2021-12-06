
from django.contrib import admin
from django.urls import path
from auapp.views import login,logout,resetpassword,changepassword,signup,createtask,viewtask,delete,feedback,contact,about
from todoapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login,name = 'login'),
    path('login/',login,name = 'login'),
    path('logout/',logout,name = 'logout'),
    path('resetpassword/',resetpassword,name = 'resetpassword'),
    path('changepassword/',changepassword,name = 'changepassword'),
    path('signup/',signup,name = 'signup'),
    path('viewtask/',viewtask,name = 'viewtask'),
    path('createtask/',createtask,name = 'createtask'),
    path('delete/<int:id>',delete,name = 'delete'),
    path('feedback/', feedback, name = 'feedback'),
    path('contact/', contact, name = 'contact'),
    path('about/', about, name = 'about'),
]
