import google.generativeai as genai

# Replace 'your-api-key-here' with your actual key
API_KEY = "AIzaSyB7xc7lapTPwUA9xPk_Ftx2ARsGCZwf8mI"

genai.configure(api_key=API_KEY)

try:
    models = genai.list_models()
    print("Available models:", [model.name for model in models])
except Exception as e:
    print("Error fetching models:", e)
