from google import genai

# Initialize client
client = genai.Client(api_key="AIzaSyB9UR1GfpYfCpzmWfa44neOruDOZdJ1M98")

# Generate content
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say hello like a trading analyst"
)

print(response.text)