from groq import Groq # type: ignore

client = Groq(api_key="YOUR_API_KEY_HERE")

message = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Hello! I am Maneesh, a SOC Analyst learning Python and AI!!"}
    ]
)

print(message.choices[0].message.content)