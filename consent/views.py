from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import MedicalAccess, ConsentRecord

@login_required
def patient_dashboard(request):
    active_accesses = []
    
    try:
        # Intentamos obtener el perfil de paciente del usuario actual
        perfil_paciente = request.user.patient
        
        # Si tiene perfil, filtramos sus accesos activos
        active_accesses = MedicalAccess.objects.filter(
            patient=perfil_paciente, 
            expires_at__gt=timezone.now()
        )
    except Exception:
        # Si el usuario NO es paciente (ej. es el Dr. Martínez) o no tiene perfil,
        # el sistema captura el error en silencio y devuelve la lista vacía.
        pass

    return render(request, 'consent/dashboard.html', {'active_accesses': active_accesses})

@login_required
def revoke_access(request, access_id):
    # Buscamos el permiso asegurándonos de que pertenezca al paciente actual
    access = get_object_or_404(MedicalAccess, id=access_id, patient=request.user)
    
    # Registramos la revocación con su respectivo hash de seguridad
    ConsentRecord.objects.create(
        patient=request.user,
        doctor_id=access.doctor.id,
        action='REVOKE'
    )
    
    # Eliminamos el permiso de la base de datos
    access.delete()
    
    return redirect('patient_dashboard')