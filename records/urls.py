from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='records-home'),
    path('patientDetail/<int:patient>', views.PatientViewLocations.as_view(), name='records-detail'),
]
