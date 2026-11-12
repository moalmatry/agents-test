from litellm import completion

# Use "gemini/gemini-2.5-flash" (or "gemini/gemini-3.1-flash-lite")
response = completion(
    model="gemini/gemini-3.8-flash",
    messages=[{"role": "user", "content": "where is cairo located?"}],
)
reply = response.choices[0].message.content
print(reply)
