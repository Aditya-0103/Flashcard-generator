import csv
import json

def parse_flashcards(raw_output):
    cards = []
    blocks = raw_output.strip().split("\nQ:")
    for block in blocks:
        if not block.strip(): continue
        q, a = block.strip().split("\nA:", 1)
        cards.append({"question": q.strip(), "answer": a.strip()})
    return cards

def export_to_csv(cards, filename="flashcards.csv"):
    with open(filename, mode="w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["question", "answer"])
        writer.writeheader()
        writer.writerows(cards)

def export_to_json(cards, filename="flashcards.json"):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(cards, f, indent=2)
