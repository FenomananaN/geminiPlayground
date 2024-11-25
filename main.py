# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key

GOOGLE_API_KEY="AIzaSyCP6u0bMmsYBh_cWGVhafpOQoxCKePOr1E"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Write a story about a magic backpack.")
print(response.text)