# ai_agent.py
import os
from google import genai
from google.genai import types

# 1. Initialize the Gemini client.
# It automatically looks for the 'GEMINI_API_KEY' environment variable.
client = genai.Client()

def generate_agent_response(user_prompt, database_context=None):
    """
    Takes a user question and optional database context, 
    feeds it to Google Gemini, and returns the response text.
    """
    
    # 2. Define the core persona instructions
    system_instruction = (
        "You are the central AI tactical agent for the CombatCompute platform. "
        "Your job is to assist the user by analyzing system metrics, logs, and data."
    )
    
    # 3. Handle data injection (RAG)
    if database_context:
        system_instruction += (
            "\n\nCRITICAL CONTEXT FROM DATABASE:\n"
            "Use the following verified system records to answer the user's request. "
            "If the records don't contain the answer, let the user know politely.\n"
            f"--- START DATABASE RECORDS ---\n{database_context}\n--- END DATABASE RECORDS ---"
        )
    else:
        system_instruction += "\n\nNote: No historical database context was provided for this request."

    try:
        # 4. Fire the request to Gemini
        # We use gemini-1.5-flash as it's optimized for speed and efficiency
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=user_prompt,
            # We pass our system rules and database context inside GenerateContentConfig
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7
            )
        )
        
        # 5. Return the text answer
        return response.text

    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        return "I encountered an error trying to process that request via my Gemini core."