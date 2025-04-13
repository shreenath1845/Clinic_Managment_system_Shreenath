from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('receptionist/dashboard/', views.receptionist_dashboard, name='receptionist_dashboard'),

    path('receptionist/add-patient/', views.add_patient, name='add_patient'),
    path('receptionist/patients/', views.patient_list, name='patient_list'),
    path('doctor/add-prescription/', views.add_prescription, name='add_prescription'),
    path('doctor/prescriptions/', views.prescription_list, name='prescription_list'),
    path('patients/delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('add-billing/', views.add_billing, name='add_billing'),
    path('list-billing/', views.list_billing, name='list_billing'),
    path('delete-billing/<int:billing_id>/', views.delete_billing, name='delete_billing'),
]
