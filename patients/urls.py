from django.urls import path
from .views import PatientListCreateAPI, patient_create, patient_list, patient_edit, patient_delete
  
urlpatterns = [
      path('', patient_list, name='patient_list'),
      path('<int:patient_id>/edit/', patient_edit, name='patient_edit'),
      path('<int:patient_id>/delete/', patient_delete, name='patient_delete'),
       path('create/', patient_create),
      path('api', PatientListCreateAPI.as_view(), name='patient_create_api'),
]