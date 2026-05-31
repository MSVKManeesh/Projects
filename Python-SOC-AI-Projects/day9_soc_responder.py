from groq import Groq # pyright: ignore[reportMissingImports]

client = Groq(api_key="YOUR_API_KEY_HERE")

# Step 1 - Read the log file
with open("auth.log", "r") as f:
    lines = f.readlines()

# Step 2 - Find suspicious IPs
failed = []
for line in lines:
    if "FAILED" in line:
        failed.append(line.strip())

# Step 3 - Send to AI for analysis
print("=== SOC INCIDENT RESPONDER ===")
print("Suspicious logs found:", len(failed))
print("Sending to AI for analysis...")
print("---")

prompt = f"You are a SOC Analyst. Analyze these failed login attempts and give a short incident report with risk level and action: {failed}"

message = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(message.choices[0].message.content)
print("=== END OF REPORT ===")