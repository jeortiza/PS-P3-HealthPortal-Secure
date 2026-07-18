from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    # Esta es la ruta que activará a tu guardia de seguridad y mostrará la historia
    path('patient/<int:patient_id>/', views.patient_record_detail, name='patient_detail'),
]