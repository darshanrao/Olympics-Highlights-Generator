# To install the Python SDK, use this CLI command:
# pip install google-generativeai

import google.generativeai as genai
from google.generativeai import GenerativeModel

API_KEY = "AIzaSyDhhr2yw8ZbQi79NI06DNyam39ZAPo1w4w"

def generate_text_with_gemini(prompt):
    genai.configure(api_key=API_KEY)

    model = GenerativeModel("gemini-1.5-flash-002")
    
    generation_config = {
        "temperature": 0,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    try:
        response = model.generate_content(
            prompt,
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# Example usage
# prompt = "The opposite of hot is"
# result = generate_text_with_gemini(API_KEY, prompt)
# print(result)

def translate(sentence:str, target_language:str) -> str:
    # Detect the source language
    detect_prompt = f"Detect the language of this sentence: '{sentence}'"
    source_language = generate_text_with_gemini(detect_prompt).strip().lower()
    
    # If source and target languages are the same, return the original sentence
    if source_language == target_language.lower():
        return sentence
    
    # Translate the sentence
    translate_prompt = f"Translate this sentence from {source_language} to {target_language}: '{sentence}' \nReturn only the translated sentence, nothing else."
    translation = generate_text_with_gemini(translate_prompt)
    
    return translation

# print(translate("Hi my name is shardul!","spanish"))