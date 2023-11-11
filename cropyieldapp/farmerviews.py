from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import FarmerRegister, LoginRegister, upload_form
from .models import Farmer, upload_img

from .prediction import model_predict
def home(request):
    return render(request, 'farmer/home.html')
def farmerviewprofile(request):
     farmer = Farmer.objects.get(user=request.user)
     return render(request, 'farmer/viewprofile.html',{'farmer': farmer})

@login_required(login_url='login_view')
def view_farmers(request):
    data = Farmer.objects.all()
    return render(request, 'admin/farmers.html', {'data': data})


def farmer_register(request):
    user_form = LoginRegister()
    customer_form = FarmerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        customer_form = FarmerRegister(request.POST,request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.is_farmer = True
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.files=request.FILES['photo']
            customer.save()
            messages.info(request, 'Registered Successfully')
            return redirect('login')
    return render(request, 'farmer/registration.html', {'user_form': user_form, 'customer_form': customer_form})



def updatefarmer(request):
    farmer = Farmer.objects.get(user=request.user)
    form = FarmerRegister(instance=farmer)
    if request.method == 'POST':
        form = FarmerRegister(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            messages.info(request, ' Profile Updated Successfully')
            return redirect('farmerviewprofile')
    return render(request, 'farmer/update.html', {'form': form})



def load_upload_page(request):
    if request.method =="POST" and 'upload_btn' in request.POST:

        form = upload_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.error(request, "Image Uploaded Sucessfully!")
        else:
            form = upload_form()
            messages.error(request, "Image not Uploaded!")

    if request.method =="POST" and 'check_btn' in request.POST:

       obj=upload_img.objects.all().last()
       scr=obj.img_upload
       new_scr='media/'+str(scr)
       print("___________the scourse _----------- ")
       print(new_scr)
       get_prediction=model_predict(new_scr)
       print("____________ the prediction ______________")
       print(get_prediction)
       context={
           "image":obj,
           "prediction":get_prediction
                }
       return render(request, 'farmer/choose.html',context)

    if request.method == "POST" and 'log_out_btn' in request.POST:

        return redirect('log_out_load')


    return render(request,'farmer/choose.html')
