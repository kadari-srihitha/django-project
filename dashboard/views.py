from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import google.generativeai as genai
import markdown_it

from doctors.models import doctor
from patients.models import patient
from medhahms import settings


@login_required
def dashboard_home(request):
    return render(request, "dashboard_home.html")


@login_required
def dashboard_ai(request):
    if request.method == 'POST':
        print("POST DATA:", request.POST)

        user_query = request.POST.get('query')

        doctors = list(doctor.objects.all().values())
        patients = list(patient.objects.all().values())

        final_query = f"""
You are the AI chatbot inside a website called medhaHMS.
You must answer ONLY questions related to this data.

Doctors:
{doctors}

Patients:
{patients}

User Question:
{user_query}
"""

        try:
            # Configure Gemini
            genai.configure(api_key=settings.GEMINI_API_KEY)

            # Create model
            model = genai.GenerativeModel('gemini-1.5-flash')

            # Generate response
            response = model.generate_content(final_query)

            result = response.text

        except Exception as e:
            print("ERROR:", str(e))
            result = f"Error: {str(e)}"

        md = markdown_it.MarkdownIt()
        answer = md.render(result)

        return render(request, "dashboard_ai.html", {
            'ai_response': answer,
            'user_query': user_query,
        })

    return render(request, "dashboard_ai.html")