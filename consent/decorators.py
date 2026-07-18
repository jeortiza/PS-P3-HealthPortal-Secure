from django.http import HttpResponseForbidden
from functools import wraps
from django.utils import timezone
from .models import MedicalAccess

def requires_patient_consent(view_func):
    """
    Bloquea el acceso si el médico no tiene consentimiento activo del paciente.
    """
    @wraps(view_func)
    def _wrapped_view(request, patient_id, *args, **kwargs):
        # El sistema verifica si existe un acceso válido y que no haya caducado
        acceso_valido = MedicalAccess.objects.filter(
            doctor=request.user,
            patient_id=patient_id,
            expires_at__gt=timezone.now()
        ).exists()

        if not acceso_valido:
            # Si no hay permiso, se levanta el muro de seguridad ABAC
            return HttpResponseForbidden(
                "<h1>ACCESO BLOQUEADO (ABAC)</h1>"
                "<p>Brecha de seguridad: No tienes el consentimiento activo de este paciente para ver su historia clínica (Ley N°29733).</p>"
            )
        
        return view_func(request, patient_id, *args, **kwargs)
    return _wrapped_view