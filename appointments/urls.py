from django.urls import path
from .views import appointment_list, appointment_edit, appointment_delete
  
urlpatterns = [
      path('', appointment_list, name='appointment_list'),
      path('<int:appointment_id>/edit/', appointment_edit, name='appointment_edit'),
      path('<int:appointment_id>/delete/', appointment_delete, name='appointment_delete'),
  ]