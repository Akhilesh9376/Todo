from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('Update/<str:pk>/',views.UpdateTask,name='Update'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('Register/',views.Register,name='Register'),
    path('login/',views.login_request,name='Login'),
    path('logout/',views.logout_request,name='logout'),
    path('Contact/',views.Contact,name='Contact'),
]