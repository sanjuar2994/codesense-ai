def calculate_score(code: str, patterns: dict, complexity: int) -> int:
    score = complexity
    score += len(patterns.get("functions", [])) * 3
    score += len(patterns.get("classes", [])) * 5
    score += len(patterns.get("loops", [])) * 2
    score += len(patterns.get("conditionals", [])) * 1
    return score