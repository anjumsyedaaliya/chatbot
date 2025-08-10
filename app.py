import google.generativeai as genai  # ✅ Use the correct import

# Your API key
API_KEY = "AIzaSyBcd89I9OfKzYKMVkS7kjswHQ4GuHrb_UU"

# Configure the genai client
genai.configure(api_key=API_KEY)

# Process prompt
def process_prompt(prompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text if hasattr(response, 'text') else response.candidates[0].content.parts[0].text
    except Exception as e:
        return f"An error occurred - {e}"

# Driver code
while True:
    prompt = input("YOU: ")
    if prompt.lower() in ["bye", "quit", "exit"]:
        print("Shutting Down")
        break
    response = process_prompt(prompt)
    print(f"CHATBOT: {response}")
