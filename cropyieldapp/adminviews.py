from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Farmer


def admin_home(request):
    return render(request, 'admin/admin_home.html')


