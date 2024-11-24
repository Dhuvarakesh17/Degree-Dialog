# chat/chatbot.py

import google.generativeai as ai
from config import API_KEY

class Chatbot:
    def __init__(self):
        ai.configure(api_key=API_KEY)
        self.model = ai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat()

    def get_response(self, user_message):
        if user_message.lower() in ['hi', 'hello', 'hey']:
            return 'Hi there! I am a student advisory chatbot for colleges. How can I assist you today?'

        response = self.chat.send_message(user_message)
        return response.text
