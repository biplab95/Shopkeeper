
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def table(request):
    return render(request,'tables.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('table/',table),
    path('', include('customer.urls')),
]

