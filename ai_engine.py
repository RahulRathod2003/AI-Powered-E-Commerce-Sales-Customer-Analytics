import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. "
        "Please create a .env file with: GROQ_API_KEY=your_key_here"
    )

# Create Groq client
client = Groq(api_key=api_key)

# Groq-hosted model to use for business insights
GROQ_MODEL = "openai/gpt-oss-120b"


def generate_business_insight(data_summary, user_question):
    """
    Generate an AI-powered business insight using the
    provided e-commerce data summary and user question.
    """

    prompt = f"""
You are an expert business data analyst.

Analyze the following e-commerce business data:

{data_summary}

User question:
{user_question}

Instructions:
- Use only the information provided.
- Do not invent or assume numbers.
- Mention relevant numbers when available.
- Explain the result in simple language.
- Give practical business recommendations when appropriate.
- Keep the response concise and professional.
"""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a professional business data analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content