def score_resume(resume_text: str, jd_keywords: list[str]) -> dict:
    text_lower = resume_text.lower()
    matched = [kw for kw in jd_keywords if kw.lower() in text_lower]
    score = len(matched) / len(jd_keywords) * 100 if jd_keywords else 0
    return {
        "score": round(score, 1),
        "matched_keywords": matched,
        "missing_keywords": [kw for kw in jd_keywords if kw not in matched],
    }
