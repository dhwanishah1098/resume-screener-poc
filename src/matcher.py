"""Match resume against job description."""
import os, json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MATCH_PROMPT = """
You are an expert recruiter. Score this resume against the job requirements.

Job Requirements:
{requirements}

Resume:
{resume_text}

Return JSON:
{{
  "match_score": 0-100,
  "matched_skills": ["..."],
  "missing_skills": ["..."],
  "experience_match": true/false,
  "education_match": true/false,
  "recommendation": "Strong/Moderate/Weak candidate - [reason]",
  "summary": "2-3 sentence assessment"
}}
"""

def match(resume_text: str, jd_requirements: dict) -> dict:
    req_str = json.dumps(jd_requirements, indent=2)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": MATCH_PROMPT.format(requirements=req_str, resume_text=resume_text[:3000])}],
        temperature=0.2,
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)
