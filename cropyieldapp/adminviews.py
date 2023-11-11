from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Farmer,Officer


def admin_home(request):
    data = Farmer.objects.all()
    dataO=Officer.objects.all()
    lenf=len(data)
    leno=len(dataO)
    return render(request, 'admin/dashboard.html',{'data2':lenf,'data1':leno})


