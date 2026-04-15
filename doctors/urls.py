from django.urls import path
from .views import DoctorListCreateApiView, doctor_list, doctor_edit, doctor_delete
  
urlpatterns = [
      path('', doctor_list, name='doctor_list'),
      path('<int:doctor_id>/edit/', doctor_edit, name='doctor_edit'),
      path('<int:doctor_id>/delete/', doctor_delete, name='doctor_delete'),
       path('api', DoctorListCreateApiView.as_view())
  ]