def parse_code(code: str) -> dict:
    lines = code.strip().splitlines()
    return {
        "lines": len(lines),
        "functions": sum(1 for line in lines if line.strip().startswith(('def ', 'function '))),
        "classes": sum(1 for line in lines if line.strip().startswith('class '))
    }