from django.test import TestCase
from .models import Patient

class PatientModelTest(TestCase):
    def setUp(self):
        # Create a test patient using the correct field names
        Patient.objects.create(
            name="John Doe",
            age=30,
            gender="Male",
            address="123 Clinic Street",
            phone="9999999999"
        )

    def test_patient_created_correctly(self):
        patient = Patient.objects.get(name="John Doe")
        self.assertEqual(patient.age, 30)
        self.assertEqual(patient.gender, "Male")
        self.assertEqual(patient.phone, "9999999999")
