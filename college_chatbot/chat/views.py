# chat/views.py

from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .chatbot import Chatbot

chatbot = Chatbot()

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')

        response_text = chatbot.get_response(user_message)
        
        return JsonResponse({'response': response_text})
