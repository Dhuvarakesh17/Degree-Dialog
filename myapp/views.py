import google.generativeai as genai
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

# Load API key
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# List of college-related keywords
COLLEGE_KEYWORDS = [
    "college", "university", "admission", "degree", "scholarship", "course", 
    "faculty", "campus", "higher education", "tuition", "student"
]

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower()

        # Check if the message contains college-related words
        if not any(keyword in user_message for keyword in COLLEGE_KEYWORDS):
            return JsonResponse({"response": "I'm here to assist with college-related inquiries only."})

        try:
            # Use a valid Gemini model
            model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
            response = model.generate_content(user_message)

            bot_reply = response.text if response.text else "Sorry, I couldn't process that."

            return JsonResponse({"response": bot_reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
