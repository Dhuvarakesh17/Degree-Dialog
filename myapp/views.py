from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import google.generativeai as genai  # Gemini API

# Load API key
import os
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(user_message)
            bot_reply = response.text if response.text else "Sorry, I couldn't process that."

            return JsonResponse({"response": bot_reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
