from django.urls import path

from . import views

urlpatterns = [
  
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login_view'),
    path('logout/', views.user_logout, name='user_logout'),
    path('create_product_details/', views.create_product_details, name='create_product_details'),
    path('list_product_details/', views.list_product_details, name='list_product_details'),
   
    path('view_product_details/<int:id>/', views.view_product_details, name='view_product_details'),
    path('enable_product_details/<int:id>/', views.enable_product_details, name='enable_product_details'),
    path('disable_product_details/<int:id>/', views.disable_product_details, name='disable_product_details'),

    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),

    path('edit_product_details/<int:id>/',views.edit_product_details,name='edit_product_details'),

   
    path('sale/', views.sale, name='sale'),
    path('patients_register/', views.patients_register, name='patients_register'),

    path('search_patient/', views.search_patient, name='search_patient'),
    path('update_patient_details/', views.update_patient_details, name='update_patient_details'),
    path('bills/', views.update_patient_details, name='update_patient_details'),
    path('add_patient/<int:id>/', views.add_patient, name='add_patient'),
    path('doctor_view/', views.doctor_view, name='doctor_view'),
    path('disable_doctor_view/<int:id>/', views.disable_doctor_view, name='disable_doctor_view'),




   





    
    



]