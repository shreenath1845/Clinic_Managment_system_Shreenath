from django.contrib import admin
from .models import Doctor, Receptionist, Patient, Prescription

admin.site.register(Doctor)
admin.site.register(Receptionist)
admin.site.register(Patient)
admin.site.register(Prescription)
