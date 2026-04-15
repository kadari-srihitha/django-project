from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime

from .models import Appointment
from patients.models import patient
from doctors.models import doctor


def appointment_list(request):
      appointments = Appointment.objects.all()
      return render(request, 'appointments.html',  {'appointments': appointments})


def appointment_edit(request, appointment_id):
      appointment_obj = get_object_or_404(Appointment, id=appointment_id)
      patients = patient.objects.all()
      doctors = doctor.objects.all()

      if request.method == 'POST':
            appointment_obj.patient_id = int(request.POST.get('patient'))
            appointment_obj.doctor_id = int(request.POST.get('doctor'))
            appointment_time_value = request.POST.get('appointment_time')
            if appointment_time_value:
                  appointment_obj.appointment_time = datetime.strptime(appointment_time_value, '%Y-%m-%dT%H:%M')
            appointment_obj.appointment_status = request.POST.get('appointment_status')
            appointment_obj.save()
            return redirect('appointment_list')

      return render(request, 'appointment_edit.html', {
            'appointment': appointment_obj,
            'patients': patients,
            'doctors': doctors,
      })


def appointment_delete(request, appointment_id):
      appointment_obj = get_object_or_404(Appointment, id=appointment_id)
      if request.method == 'POST':
            appointment_obj.delete()
            return redirect('appointment_list')
      return render(request, 'appointment_delete_confirm.html', {'appointment': appointment_obj})