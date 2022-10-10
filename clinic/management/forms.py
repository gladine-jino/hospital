from dataclasses import fields
from django import forms
from msilib.schema import Class
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import User,Items_saled,ProductDetails,PatientDetails





class RegisterForm(UserCreationForm):
   password2 =forms.CharField(label = ' Confirm  Password',required=True,widget=forms.PasswordInput)
   class Meta:
        model=User
        fields=['first_name','last_name','username','email','is_admin','is_customer']
        labels={'email':'Email'}

class InputForm(forms.ModelForm):   
   class Meta:
        model=Items_saled
        fields='__all__'

class ProductDetailsForm(forms.ModelForm):  
   # my_field = DateField(widget = AdminDateWidget) 
   # expiry_date = forms.DateField(attrs={'type':'date'})
   class Meta:
      model=ProductDetails
      fields=['product_name','product_id','product_quantity','product_price','expiry_date']
 

      widgets = { 'expiry_date' : forms.DateInput(attrs={'type':'date',}),}

class PatientDetailsForm(forms.ModelForm):   
   class Meta:
        model=PatientDetails
        fields='__all__'



