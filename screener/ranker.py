def rank_candidates(scored: list[dict]) -> list[dict]:
    return sorted(scored, key=lambda x: x['score'], reverse=True)
