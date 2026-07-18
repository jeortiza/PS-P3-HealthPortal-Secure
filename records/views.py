from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from consent.decorators import requires_patient_consent
from patients.models import Patient
from .models import MedicalRecord

# Aquí colocamos nuestros escudos de seguridad en orden
@login_required
@requires_patient_consent
def patient_record_detail(request, patient_id):
    """
    Vista protegida de la historia clínica.
    Solo se ejecuta si el decorador ABAC da luz verde.
    """
    # 1. Buscamos al paciente por su ID
    patient = get_object_or_404(Patient, id=patient_id)
    
    # 2. Traemos su historia clínica cifrada de la base de datos
    records = MedicalRecord.objects.filter(patient=patient)
    
    # 3. Enviamos los datos a la plantilla HTML
    return render(request, 'patients/detail.html', {
        'patient': patient,
        'records': records
    })