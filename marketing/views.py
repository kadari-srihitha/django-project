from django.shortcuts import render

# Create your views here.
def home(request):
      return render(request, "marketing.html")
def contact(request):
      return render(request, "contact.html")