# Resume Screener POC

> ⚠️ Work in progress

An LLM-powered tool to match resumes against job descriptions and score candidates automatically.

## Goal
Reduce manual resume screening time by 80% using semantic matching + LLM scoring.

## Status
- [x] PDF text extraction
- [x] JD parsing and requirement extraction
- [x] Resume → JD matching score
- [ ] Batch processing UI
- [ ] ATS integration

## Usage
```bash
python screen.py --resume resume.pdf --jd job_description.txt
```

## Output
```json
{
  "match_score": 82,
  "matched_skills": ["Python", "SQL", "Data Analysis"],
  "missing_skills": ["Tableau"],
  "recommendation": "Strong candidate - recommend interview",
  "summary": "..."
}
```
