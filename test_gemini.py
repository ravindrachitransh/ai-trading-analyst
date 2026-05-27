import os

from google import genai

# Initialize client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Generate content
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say hello like a trading analyst"
)

print(response.text)