from django.shortcuts import render, redirect, get_object_or_404

from patients.forms import PatientForm
from .models import patient

def patient_list(request):
      patients = patient.objects.all()
      return render(request, 'list.html',  {'patients': patients})

def patient_edit(request, patient_id):
      patient_obj = get_object_or_404(patient, id=patient_id)
      
      if request.method == 'POST':
            patient_obj.name = request.POST.get('name')
            patient_obj.phone = request.POST.get('phone')
            patient_obj.email = request.POST.get('email')
            patient_obj.save()
            return redirect('patient_list')
      
      return render(request, 'edit.html', {'patient': patient_obj})


def patient_delete(request, patient_id):
      patient_obj = get_object_or_404(patient, id=patient_id)
      if request.method == 'POST':
            patient_obj.delete()
            return redirect('patient_list')
      return render(request, 'delete_confirm.html', {'patient': patient_obj})
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/patients/')
    else:
        form = PatientForm()
    return render(request, "patient_create.html", {'form': form})

from rest_framework.generics import ListCreateAPIView
from .serializers import PatientSerializer

class PatientListCreateAPI(ListCreateAPIView):
    queryset = patient.objects.all()
    serializer_class = PatientSerializer