from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from google import genai
import markdown_it

from doctors.models import doctor
from medhahms import settings
from patients.models import patient
  
# Create your views here.
@login_required
def dashboard_home(request):
    return render(request, "dashboard_home.html")
@login_required
def dashboard_ai(request):
    if request.method == 'POST':
        print("POST DATA:", request.POST)

        user_query = request.POST.get('query')

        client = genai.Client(api_key=settings.GEMINI_API_KEY)

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

        response = None 

        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=final_query,
            )

            print("FULL RESPONSE:", response)

            
            if hasattr(response, "text") and response.text:
                result = response.text
            else:
                try:
                    result = response.candidates[0].content.parts[0].text
                except:
                    result = " No response from AI"

        except Exception as e:
            print("ERROR:", str(e))
            result = f"Error: {str(e)}"

       
        md = markdown_it.MarkdownIt()
        answer = md.render(result)

        return render(request, "dashboard_ai.html", {
            'ai_response': answer,
            'user_query': user_query,
        })

    return render(request, "dashboard_ai.html", {
        'ai_response': None,
        'user_query': None,
    })