from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor, Receptionist, Patient, Prescription, Billing
from .forms import PatientForm, PrescriptionForm, BillingForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if hasattr(user, 'doctor'):
                return redirect('doctor_dashboard')
            elif hasattr(user, 'receptionist'):
                return redirect('receptionist_dashboard')
            else:
                messages.error(request, "Role not assigned.")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def doctor_dashboard(request):
    if not hasattr(request.user, 'doctor'):
        return redirect('login')
    return render(request, 'doctor_dashboard.html')



@login_required
def receptionist_dashboard(request):
    if not hasattr(request.user, 'receptionist'):
        return redirect('login')
    return render(request, 'receptionist_dashboard.html')



@login_required
def add_billing(request):
    if not hasattr(request.user, 'receptionist'):
        return redirect('login')

    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Billing added successfully.")
            return redirect('list_billing')
    else:
        form = BillingForm()
    return render(request, 'add_billing.html', {'form': form})


@login_required
def list_billing(request):
    if not hasattr(request.user, 'receptionist'):
        return redirect('login')

    billings = Billing.objects.all()
    return render(request, 'list_billing.html', {'billings': billings})


@login_required
def delete_billing(request, billing_id):
    if not hasattr(request.user, 'receptionist'):
        return redirect('login')

    billing = get_object_or_404(Billing, id=billing_id)
    billing.delete()
    return redirect('list_billing')



@login_required
def add_patient(request):
    if not hasattr(request.user, 'receptionist'):
        return redirect('login')

    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Patient added successfully.")
        return redirect('patient_list')
    return render(request, 'add_patient.html', {'form': form})


@login_required
def patient_list(request):
    if not hasattr(request.user, 'receptionist'):
        return redirect('login')

    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})


@login_required
def delete_patient(request, patient_id):
    if not hasattr(request.user, 'receptionist'):
        return redirect('login')

    patient = get_object_or_404(Patient, id=patient_id)
    patient.delete()
    return redirect('patient_list')



@login_required
def add_prescription(request):
    if not hasattr(request.user, 'doctor'):
        return redirect('login')

    form = PrescriptionForm(request.POST or None)
    if form.is_valid():
        prescription = form.save(commit=False)
        prescription.doctor = request.user.doctor
        prescription.save()
        messages.success(request, "Prescription added successfully.")
        return redirect('prescription_list')
    return render(request, 'add_prescription.html', {'form': form})


@login_required
def prescription_list(request):
    if not hasattr(request.user, 'doctor'):
        return redirect('login')

    prescriptions = Prescription.objects.filter(doctor=request.user.doctor)
    return render(request, 'prescription_list.html', {'prescriptions': prescriptions})
