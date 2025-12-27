BANNED_TERMS = ["kill", "bomb", "suicide"]

def validate_input(prompt: str) -> None:
    if any(term in prompt.lower() for term in BANNED_TERMS):
        raise ValueError("Unsafe input detected")
