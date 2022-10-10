from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import ProductDetails,PatientDetails,TodayPatients
from .forms import RegisterForm, InputForm,ProductDetailsForm,PatientDetailsForm
from django.contrib.auth import login as log
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from datetime import timezone
import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q



#user views

def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        is_customer=request.POST.get("customer")
        if is_customer==None:
            is_customer=0
        is_admin=request.POST.get("admin")
        if is_admin==None:
            is_admin=0
        print(is_admin) 
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Account created successfully') 
            return redirect('login_view')
        else:
            return render(request,'management/register.html', {'form':form})             
    else:        
        form = RegisterForm()
        return render(request, 'management/register.html', {'form':form}) 


def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST) 
        if form.is_valid():
            username=form.cleaned_data.get('username')            
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)            
            if user:    
                if user.is_admin :
                    log(request,user)
                    return redirect('doctor_view')
                elif user.is_customer:
                    log(request,user)
                    return redirect('patient_register')
                else:
                    return HttpResponse("invalid")                  
            else:
                messages.error(request,'Not user')    
                return render(request,'management/login.html',{'form':form})          
        else:
            print(form.errors)
            return render(request,'management/login.html',{'form':form})     
    else:      
        form=AuthenticationForm()
        return render(request,'management/login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('register')



# product views

def create_product_details(request):
    
    if request.method=="POST":
        form = ProductDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'created successfully') 
            return redirect('list_product_details')
        else:
            form = ProductDetailsForm()
            return render(request,'management/create_product_details.html',{'form':form})         
       
    else:
        form = ProductDetailsForm()
        return render(request,'management/create_product_details.html',{'form':form})



def list_product_details(request):
    x=  ProductDetails.objects.all()
   
    if request.method=="POST": 
        selected_date=request.POST.get("date") 
        print(selected_date)
        date_time_obj = datetime.datetime.strptime( selected_date, '%Y-%m-%d').date()
        print( date_time_obj)
        result= ProductDetails.objects.filter(created_at__date__gte= date_time_obj)
        print(result)        
        return render(request,'management/list_product_details.html',{'x':result})
    else:
        
        return render(request,'management/list_product_details.html',{'x':x})


@login_required(login_url='login_view')
def view_product_details(request,id):
    if request.user.is_admin:
     x=  ProductDetails.objects.get(id=id)
     return render(request,'management/view_product_details.html',{'x':x})
    
    else:
        return HttpResponse('not permit')



def sale(request):
    if request.method=="POST":
        form=InputForm(request.POST)
        if form.is_valid():
            x=form.save()           
            y=x.items_saled            
            pro=ProductDetails.objects.get(id=x.item.id)
            pro.product_value=pro.product_value-y
            pro.save()         
        return redirect('view_product_details')
    else:
       form=InputForm()
       return render(request,'management/sale.html',{'form':form}) 


@login_required(login_url='login_view')
def edit_product_details(request,id):
    if request.user.is_admin:
        edit = ProductDetails.objects.get(id=id)
        if request.method=="POST":  

            form = ProductDetailsForm(instance =edit)
            # edit.product_name = request.POST.get("product_name")
            # edit.product_id = request.POST.get("product_id")
            # edit.product_quantity= request.POST.get("product_quantity")
            # edit.product_price = request.POST.get("product_price")
            # date=request.POST.get("date")
            # print('hi')
            # print(str(date))
            # if date=='':
            #     edit.expiry_date=request.POST.get("expiry_date")
            # else:
            #     edit.expiry_date=date

            # edit.save()    
            # print(edit)
        
            return render(request,"management/view_product_details.html",{'edit':edit, 'form':form})
          

        else:
            form = ProductDetailsForm(instance =edit)
            return render(request,"management/edit_product_details.html",{'edit':edit, 'form':form})
    else:
        return HttpResponse('not permit')



def delete_product(request,id):
    x = ProductDetails.objects.get(id=id)
    x.delete()
    return redirect('list_product_details')


@login_required(login_url='login_view')
def enable_product_details(request,id):
    if request.user.is_admin:
        enable = ProductDetails.objects.get(id=id)
        enable.is_active=True
        enable.save()
        return redirect('list_product_details')        
    # return render(request,"management/edit_product_details.html",{'enable':enable, 'form':form})
    else:
        return HttpResponse('not permit')


@login_required(login_url='login_view')
def disable_product_details(request,id):
    if request.user.is_admin:
        disable=ProductDetails.objects.get(id=id)
        disable.is_active=False
        disable.save()
        return redirect('list_product_details')  
    else:
        return HttpResponse('not permit')  


# patient views


def patients_register(request):
    if request.method=="POST":
        form = PatientDetailsForm(request.POST)        
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Details created successfully') 
            return redirect('search_patient')
        else:
            print(form.errors)
            messages.info(request,'User Registration Failed')
            return render(request,'management/patient_register.html',{'patient_id':increment_patient_id(),'form': form})     
    else:
        
     return render(request,'management/patient_register.html',{'patient_id':increment_patient_id()})  


def increment_patient_id():
    last = PatientDetails.objects.last()
    if last == None:
        last = 0
    else:
        last = last.id
    last+=1
    return ( "DB022" "%03d" % last)


def search_patient(request):
    x=  PatientDetails.objects.all()
    if request.method=="POST": 
        patient_id=request.POST.get("patient_id") 
        patient_name=request.POST.get("patient_name") 
        Phone_number=request.POST.get("Phone_number") 
        result= PatientDetails.objects.filter(Q(patient_name=patient_name)| Q(Phone_number=Phone_number)| Q(patient_id=patient_id))
        print(result)        
        return render(request,'management/search_patient.html',{'x':result})              
        
    else:        
        return render(request,'management/search_patient.html',{'x':x})  


def update_patient_details(request):
        
    if request.method=="POST": 
         update = PatientDetails.objects.get(id=request.POST.get("ob"))
         update.patient_name=request.POST.get("patient_name")
         update.Address=request.POST.get("Address")
         update.Age=request.POST.get("Age")
         update.Phone_number=request.POST.get("Phone_number")
         update.save()         
         return redirect('search_patient')        
    
    else:
   
        return render(request,"management/search_patient.html")


def bills(request):
  
    return render(request, "management/bills.html")


def add_patient(request,id):
     add_patient=PatientDetails.objects.get(id=id)
     TodayPatients.objects.create(patient=add_patient)
     return redirect('search_patient')

def doctor_view(request):
    x=  TodayPatients.objects.filter(created_at__contains=datetime.datetime.today().date())
   
    return render(request,"management/doctor_view.html",{'x':x})

def disable_doctor_view(request,id):
    disable_view=TodayPatients.objects.get(id=id)
    disable_view.is_active=True
    disable_view.save()
   
   
       

    return redirect('doctor_view')

# def add_new_history(request,id):


    




    

  





     
    
    



   



            


