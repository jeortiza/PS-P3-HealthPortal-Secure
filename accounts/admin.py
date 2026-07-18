from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin  # <-- Agregamos esta importación

# Obtenemos tu modelo de usuario personalizado
User = get_user_model()

# Lo registramos usando la clase especial UserAdmin
admin.site.register(User, UserAdmin)