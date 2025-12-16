"""Extract text from PDF resumes."""
import pdfplumber
from pathlib import Path

def extract_text(pdf_path: str) -> str:
    text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return '\n'.join(text)

def extract_sections(text: str) -> dict:
    """Heuristic section detection."""
    sections = {}
    current = "general"
    lines = text.splitlines()
    keywords = {
        "experience": ["experience", "work history", "employment"],
        "education": ["education", "qualifications", "academic"],
        "skills": ["skills", "technical skills", "competencies"],
        "summary": ["summary", "profile", "objective"]
    }
    for line in lines:
        low = line.lower().strip()
        for section, kws in keywords.items():
            if any(kw in low for kw in kws):
                current = section
                break
        sections.setdefault(current, []).append(line)
    return {k: '\n'.join(v) for k, v in sections.items()}
