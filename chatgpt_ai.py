import openai

# Set your API key
openai.api_key = "Replace with your key"  # Replace with your key

def chat_with_ai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use gpt-4 if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response['choices'][0]['message']['content'].strip()
        return reply

    except Exception as e:
        return "Sorry, I couldn't connect to the AI right now."
