from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('revoke/<int:access_id>/', views.revoke_access, name='revoke_access'),
]