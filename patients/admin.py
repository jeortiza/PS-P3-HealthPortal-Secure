from django.contrib import admin
from .models import Patient

# Registramos el modelo Patient para verlo en el panel
admin.site.register(Patient)