"""Parse job description and extract requirements."""
import os, json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

JD_PARSE_PROMPT = """
Extract requirements from this job description in JSON format:
{{
  "required_skills": ["..."],
  "preferred_skills": ["..."],
  "min_experience_years": 0,
  "education_required": "...",
  "key_responsibilities": ["..."]
}}

Job Description:
{jd_text}
"""

def parse_jd(jd_text: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": JD_PARSE_PROMPT.format(jd_text=jd_text)}],
        temperature=0.1,
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)
