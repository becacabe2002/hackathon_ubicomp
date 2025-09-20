import spacy
from typing import List, Dict, Tuple

# Load the small English model
nlp = spacy.load("en_core_web_sm")

TARGET_LABELS = {"PERSON", "ORG", "MONEY"}

def anonymize_text(text: str) -> Tuple[str, List[Dict]]:
    """
    Anonymize entities in the text for labels PERSON, ORG, MONEY.
    Returns the anonymized text and a list of entities.
    """
    doc = nlp(text)
    entities = []
    anonymized_text = text
    offset = 0  # Track offset due to replacements
    label_counters = {label: 1 for label in TARGET_LABELS}

    # Collect entities to anonymize
    ents_to_anonymize = [
        ent for ent in doc.ents if ent.label_ in TARGET_LABELS
    ]

    # Sort by start_char to replace from left to right
    ents_to_anonymize.sort(key=lambda ent: ent.start_char)

    for ent in ents_to_anonymize:
        original = ent.text
        label = ent.label_
        start = ent.start_char + offset
        end = ent.end_char + offset

        # Create anonymized token
        token = f"[{label}_{label_counters[label]}]"
        label_counters[label] += 1

        # Replace in text
        anonymized_text = (
            anonymized_text[:start] + token + anonymized_text[end:]
        )

        # Update offset for next replacements
        offset += len(token) - len(original)

        # Record entity info
        entities.append({
            "text": original,
            "label": label,
            "start": ent.start_char,
            "end": ent.end_char
        })

    return {
        "anonymized_text": anonymized_text
    }

# Example usage
if __name__ == "__main__":
    text = "I am Bobby JacksOn, I have my insurance from Blue Cross and I have $18856.2813059782 billing value."
    res = anonymize_text(text)
    print(res)
