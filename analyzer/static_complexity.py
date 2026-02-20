def calculate_complexity(code: str) -> int:
    score = 0
    loops = ['for ', 'while ']
    conditionals = ['if ', 'elif ', 'else:']
    functions = ['def ', 'function ']

    for line in code.splitlines():
        if any(line.strip().startswith(l) for l in loops):
            score += 2
        if any(line.strip().startswith(c) for c in conditionals):
            score += 1
        if any(line.strip().startswith(f) for f in functions):
            score += 3
    return score