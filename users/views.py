from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
import resend
from django.contrib import messages

from medhahms import settings
def signup(request):
      if request.method == 'POST':
          username = request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          user = User.objects.create_user(
              username=username,
              email=email,
              password=password
          )
        #   resend.api_key = settings.RESEND_API_KEY
        #   send_mail(
        #         subject='Welcome to MedhaHMS',
        #         message='Thank you for signing up for MedhaHMS!',
        #         from_email=settings.DEFAULT_FROM_EMAIL,
        #         recipient_list=[user.email],
        #         fail_silently=False,
        #   )

          login(request, user)
          return render(request, 'email_sent.html', {'email': user.email})
      else:
          return render(request, 'user.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        print("AUTH USER:", user) 

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')
