import os
from dotenv import load_dotenv
from groq import Groq
from app.retriever import retriever

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = os.getenv("MODEL_NAME", "openai/gpt-oss-120b")


# Greeting handler
def is_greeting(query: str):
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    return query.lower().strip() in greetings


def generate_answer(query: str):

    # Step 1: Greetings
    if is_greeting(query):
        return "Hello! How can I help you today?"

    # Step 2: Retrieve context
    context = retriever(query)

    # Fix: Convert list -> string
    if isinstance(context, list):
        context = " ".join([str(doc) for doc in context])

    # Step 3: Empty context handling
    if not context or len(context.strip()) == 0:
        return (
            "I'm sorry, I couldn't find any relevant information "
            "in the documents."
        )

    # Step 4: Build prompt
    prompt = f"""
Context:
{context}

User Question:
{query}
"""

    # Step 5: Generate response
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": """
You are an intelligent and professional RAG assistant.

STRICT RULES:

1. Answer ONLY from the given context.
2. If answer is clearly present → respond accurately.
3. If context is related but answer not found → say:
   "I don't know based on the provided document."

4. If question is unrelated to context → say:
   "I'm sorry, I can only answer questions related to the provided documents."

5. Do NOT:
   - Add outside knowledge
   - Guess answers
   - Hallucinate

6. Keep answers:
   - Clear
   - Short
   - Professional
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content