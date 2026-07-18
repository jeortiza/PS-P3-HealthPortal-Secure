from django.contrib import admin
from .models import MedicalAccess, ConsentRecord

admin.site.register(MedicalAccess)
admin.site.register(ConsentRecord)