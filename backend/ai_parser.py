import google.generativeai as genai
import re
import json

# configure Gemini API
genai.configure(api_key="AIzaSyBfC-YhL2LBWP9FfxGHn2RT695Jb7SzSbA")

model = genai.GenerativeModel("gemini-1.5-flash")


def parse_expense(text):

    try:

        prompt = f"""
Extract expense information from the sentence.

Return JSON in this format:
{{"amount": number, "category": "string"}}

Sentence: {text}
"""

        response = model.generate_content(prompt)

        result = response.text

        print("Gemini response:", result)

        match = re.search(r"\{.*\}", result)

        if match:
            return json.loads(match.group())

    except Exception as e:
        print("Gemini failed:", e)

    # fallback parser if AI fails

    amount_match = re.search(r"\d+", text)

    if amount_match:
        amount = float(amount_match.group())
    else:
        amount = 0

    text_lower = text.lower()

    # smart category detection

    if "uber" in text_lower or "ride" in text_lower or "taxi" in text_lower or "bus" in text_lower:
        category = "transport"

    elif "coffee" in text_lower or "food" in text_lower or "lunch" in text_lower or "dinner" in text_lower or "groceries" in text_lower:
        category = "food"

    elif "electricity" in text_lower or "bill" in text_lower or "rent" in text_lower:
        category = "bills"

    elif "shopping" in text_lower or "clothes" in text_lower:
        category = "shopping"

    else:
        category = "other"

    return {
        "amount": amount,
        "category": category
    }