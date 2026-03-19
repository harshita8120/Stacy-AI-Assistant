import os
from dotenv import load_dotenv
from google import genai

# Load the environment variables from the .env file
load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def geminiResponse(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=text,
    )

    return response.text



