def calculate_risk(
    dns,
    ssl,
    age,
    header_score
):

    score = 0

    if not dns:
        score += 40

    if not ssl:
        score += 30

    if age is not None:

        if age < 1:
            score += 20

    if header_score < 2:
        score += 10

    if score <= 30:
        level = "Low"

    elif score <= 60:
        level = "Medium"

    else:
        level = "High"

    return {
        "score": score,
        "level": level
    }