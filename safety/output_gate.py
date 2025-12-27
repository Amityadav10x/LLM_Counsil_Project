def validate_output(text: str) -> list:
    risks = []
    if "guaranteed" in text.lower():
        risks.append("Overconfident language detected")
    return risks
