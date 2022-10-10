from sqlite3 import Date
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is_customer', default=False)


class ProductDetails(models.Model):
    product_name= models.CharField(max_length=30)
    product_id= models.CharField(max_length=30)
    product_quantity= models.CharField(max_length=30)
    product_price= models.CharField(max_length=30)
    expiry_date=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=   models.BooleanField('Is active', default=False)  
 

class Items_saled(models.Model):
    item = models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    items_saled=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PatientDetails(models.Model):
    patient_id= models.CharField(max_length=30)
    patient_name= models.CharField(max_length=30)
    fathers_name= models.CharField(max_length=30)
    Age= models.IntegerField()
    Date_of_birth= models.DateField()
    Gender= models.CharField(max_length=30)
    Address= models.TextField(max_length=30)
    Phone_number = models.IntegerField()
     


class TodayPatients(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=   models.BooleanField('Is active', default=False) 


   







