import hashlib
from django.db import models
from django.conf import settings
from patients.models import Patient  # <-- Ruta ajustada a tu estructura real
from django.utils import timezone

class MedicalAccess(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='medical_accesses')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_accesses')
    granted_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Acceso Activo: Dr. {self.doctor.username} -> Paciente {self.patient.dni}"

    def is_active(self):
        return timezone.now() < self.expires_at

class ConsentRecord(models.Model):
    ACTION_CHOICES = [
        ('GRANT', 'Otorgar Acceso'),
        ('REVOKE', 'Revocar Acceso'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    integrity_hash = models.CharField(max_length=64, blank=True, help_text="Firma criptográfica SHA-256")

    def save(self, *args, **kwargs):
        # Generar el hash de integridad inmutable justo antes de guardar en disco
        if not self.integrity_hash:
            # Combinamos los datos críticos para crear una "huella digital" única
            raw_data = f"{self.patient.id}-{self.doctor.id}-{self.action}-{timezone.now().timestamp()}"
            self.integrity_hash = hashlib.sha256(raw_data.encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.action} - Paciente {self.patient.dni} a Dr. {self.doctor.username}"