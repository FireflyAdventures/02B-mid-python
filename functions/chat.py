import google.generativeai as genai
from decouple import config

genai.configure(api_key=config("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
	response = model.generate_content(question)
	return response.text

