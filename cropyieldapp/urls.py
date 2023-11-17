from django.urls import path

from . import views, adminviews, officerviews, farmerviews

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),

    path('admin_home/', adminviews.admin_home, name='admin_home'),

    path('farmer_register/', farmerviews.farmer_register, name='farmer_register'),
    path('farmerviewprofile/', farmerviews.farmerviewprofile, name='farmerviewprofile'),
    path('farmers_view/', farmerviews.view_farmers, name='farmers_view'),
    path('updatefarmer', farmerviews.updatefarmer, name='updatefarmer'),
    path('home/', farmerviews.home, name='home'),
    path('load_upload_page/', farmerviews.load_upload_page, name="load_upload_page"),
    path('enquiry/', farmerviews.enquiry_add, name="enquiry"),
    path('enquiry_view/', farmerviews.enquiry_view, name="enquiry_view"),



    path('officer_home/', officerviews.officer_home, name='officer_home'),
    path('officer_register/', officerviews.officer_register, name='officer_register'),
    path('view_officer/', officerviews.view_officer, name='view_officer'),
    path('remove_officer/<int:id>/', officerviews.remove_officer, name='remove_officer'),
    path('enquiry_view_of/', officerviews.enquiry_view, name="enquiry_view"),

]