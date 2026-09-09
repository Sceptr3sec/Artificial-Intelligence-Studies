from typing import Dict, List
from openai import OpenAI

SYSTEM_PROMPT = """You are a knowledgeable NASA space mission expert assistant.
You help users understand historical NASA missions (such as Apollo 11, Apollo 13,
and the Challenger mission) using the provided source material as your primary
reference.

Guidelines:
- Base your answers primarily on the CONTEXT provided below, which comes from
  real NASA transcripts, reports, and archival documents.
- If the context does not contain enough information to answer confidently,
  say so honestly rather than guessing or inventing facts.
- Be clear, concise, and factual. Use plain language a curious member of the
  public could follow, while still being technically accurate.
- When helpful, mention which mission or document the information comes from.
"""

def generate_response(openai_key: str, user_message: str, context: str,
                     conversation_history: List[Dict], model: str = "gpt-3.5-turbo") -> str:
    """Generate response using OpenAI with context"""

    # Build the system message, injecting retrieved context (if any)
    if context:
        system_content = f"{SYSTEM_PROMPT}\n\nCONTEXT:\n{context}"
    else:
        system_content = f"{SYSTEM_PROMPT}\n\nCONTEXT:\nNo relevant documents were found for this question."

    messages = [{"role": "system", "content": system_content}]

    # Add prior conversation turns so the model has memory of the chat
    for turn in conversation_history:
        role = turn.get("role")
        content = turn.get("content")
        if role in ("user", "assistant") and content:
            messages.append({"role": role, "content": content})

    # Add the current user question last
    messages.append({"role": "user", "content": user_message})

    # Create the OpenAI client and send the request
    client = OpenAI(api_key=openai_key)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.3,
    )

    return response.choices[0].message.content
