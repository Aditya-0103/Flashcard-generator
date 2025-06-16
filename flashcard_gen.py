import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure the Gemini client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

def generate_flashcards(
    content: str,
    subject: str = "General",
    include_difficulty: bool = False,
    include_grouping: bool = False,
    translate_to: str = None
) -> list:
    """
    Generate flashcards from content using Gemini 1.5 Flash model.
    Returns a list of dicts with keys: question, answer, etc.
    """

    prompt = f"""You are a helpful tutor creating flashcards.

Your task is to generate 10–15 Q&A flashcards based on the text below.

Each flashcard should follow this format:
Q: <question>
A: <factual, self-contained answer>

Subject: {subject}
"""

    if include_difficulty:
        prompt += "\nInclude difficulty level for each card (Easy, Medium, Hard)."
    if include_grouping:
        prompt += "\nGroup flashcards under topic headings if possible."
    if translate_to:
        prompt += f"\nAlso include a translation in {translate_to}."

    prompt += f"\n\nCONTENT:\n\"\"\"\n{content}\n\"\"\""

    try:
        response = model.generate_content(prompt)
        output = response.text
        print("LLM Output:\n", output)  # For debugging
        flashcards = parse_flashcards_from_text(output)
        return flashcards
    except Exception as e:
        print("Error during Gemini call:", e)
        return []

def parse_flashcards_from_text(text: str) -> list:
    flashcards = []
    cards = text.strip().split("Q:")
    for card in cards[1:]:
        parts = card.strip().split("A:")
        if len(parts) < 2:
            continue
        question = parts[0].strip()
        answer = parts[1].strip()
        flashcards.append({"question": question, "answer": answer})
    return flashcards
