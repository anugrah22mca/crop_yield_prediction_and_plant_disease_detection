import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Farmer, Login, Officer ,upload_img ,Chat


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')

class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label='password')
    password2=forms.CharField(widget=forms.PasswordInput,label='confirm password')

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')
class FarmerRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Farmer
        fields = ('name', 'contact_no', 'email', 'address','photo','Aadhaar_id')


class OfficerRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Officer
        fields = ('name', 'contact_no', 'email', 'address','office_location','office_name','photo','id_card')



class upload_form(forms.ModelForm):

    class Meta:
        model=upload_img
        fields=['img_upload']


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('desc',)