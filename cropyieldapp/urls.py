from django.urls import path

from diseasedetection.cropyieldapp import views

urlpatterns = [
    path('', views.home, name='home'),
]