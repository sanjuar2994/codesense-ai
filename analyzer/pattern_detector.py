import re

def detect_patterns(code: str) -> dict:
    patterns = {
        "functions": re.findall(r'\bdef\s+\w+\b|\bfunction\s+\w+\b', code),
        "classes": re.findall(r'\bclass\s+\w+\b', code),
        "loops": re.findall(r'\bfor\b|\bwhile\b', code),
        "conditionals": re.findall(r'\bif\b|\belif\b|\belse\b', code),
    }
    return patterns