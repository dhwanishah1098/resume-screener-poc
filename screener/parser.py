import re

def extract_contact_info(text: str) -> dict:
    email_match = re.search(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", text)
    phone_match = re.search(r"(\+?\d[\d\s\-]{7,}\d)", text)
    return {
        "email": email_match.group() if email_match else None,
        "phone": phone_match.group().strip() if phone_match else None,
    }

def extract_years_experience(text: str) -> int | None:
    m = re.search(r"(\d+)\+?\s+year", text, re.IGNORECASE)
    return int(m.group(1)) if m else None
