import os
from groq import Groq
from utils.prompts import generate_ai_prompt
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------- Code Analysis ----------------
def analyze_code_with_ai(code: str) -> str:
    prompt = generate_ai_prompt(code)
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="openai/gpt-oss-20b"
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI analysis error: {e}"

# ---------------- Context-Aware Chatbot ----------------
def chat_with_ai(user_input: str, code_context: str = None) -> str:
    """
    If code_context is provided, the bot will use it to answer questions about the uploaded code.
    """
    if code_context:
        prompt = f"You are a coding tutor. The user has the following code:\n{code_context}\nAnswer the user's question based on this code.\nQuestion: {user_input}"
    else:
        prompt = f"You are a coding tutor. Answer the user's question:\n{user_input}"

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="openai/gpt-oss-20b"
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI chat error: {e}"