from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('Update/<str:pk>/',views.UpdateTask,name='Update'),
    path('delete/<str:pk>/',views.delete,name='delete'),
]