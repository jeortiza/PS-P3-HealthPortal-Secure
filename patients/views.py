from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Patient
from records.models import MedicalRecord

@login_required
def home(request):
    # ESCUDO 2FA: Verificamos si el usuario tiene configurado su Doble Factor
    if not getattr(request.user, 'totp_secret', None):
        return HttpResponseForbidden(
            "<h1>🛑 ACCESO BLOQUEADO</h1>"
            "<p>Brecha de seguridad detectada: Este usuario no tiene configurado el Doble Factor de Autenticación (2FA). "
            "Por políticas estrictas, el acceso a los datos médicos (PHI) ha sido denegado.</p>"
        )

    # Obtenemos el paciente y su historial para la demo
    paciente = Patient.objects.first()
    registro = MedicalRecord.objects.filter(patient=paciente).first()
    
    return render(request, 'patients/home.html', {
        'paciente': paciente,
        'registro': registro
    })