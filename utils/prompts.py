def generate_ai_prompt(code: str) -> str:
    return f"""
You are an expert AI code reviewer.
Analyze the following code:

{code}

Please provide:
1. Syntax and logical errors.
2. Suggestions to improve readability and modularity.
3. Identify bad coding practices.
4. Evaluate placement readiness.
5. Tips to improve for interviews.
"""