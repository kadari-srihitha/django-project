from django.shortcuts import render, redirect, get_object_or_404
from .models import doctor

def doctor_list(request):
      doctors = doctor.objects.all()
      return render(request, 'doctors.html',  {'doctors': doctors})


def doctor_edit(request, doctor_id):
      doctor_obj = get_object_or_404(doctor, id=doctor_id)
      if request.method == 'POST':
            doctor_obj.name = request.POST.get('name')
            doctor_obj.specialization = request.POST.get('specialization')
            doctor_obj.save()
            return redirect('doctor_list')
      return render(request, 'doctor_edit.html', {'doctor': doctor_obj})


def doctor_delete(request, doctor_id):
      doctor_obj = get_object_or_404(doctor, id=doctor_id)
      if request.method == 'POST':
            doctor_obj.delete()
            return redirect('doctor_list')
      return render(request, 'doctor_delete_confirm.html', {'doctor': doctor_obj})

from rest_framework.generics import ListCreateAPIView
from .serializer import DoctorSerializer

class DoctorListCreateApiView(ListCreateAPIView):
    queryset = doctor.objects.all()
    serializer_class = DoctorSerializer