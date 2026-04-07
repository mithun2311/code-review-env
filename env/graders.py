def grade(comments, expected_issues):
    total_score = 0
    penalty = 0

    for issue in expected_issues:
        issue_type = issue["type"]
        severity = issue["severity"]

        found = False
        explanation = False

        for c in comments:
            c_lower = c.lower()

            # detection
            if issue_type in c_lower:
                found = True

                # explanation quality
                if any(word in c_lower for word in ["because", "issue", "problem", "risk", "vulnerability"]):
                    explanation = True

        weight = 1.0 if severity == "high" else 0.5

        if found:
            total_score += 0.5 * weight
        if explanation:
            total_score += 0.5 * weight

    # false positive penalty
    for c in comments:
        if not any(issue["type"] in c.lower() for issue in expected_issues):
            penalty += 0.1

    final_score = max(total_score - penalty, 0)

    score = final_score / len(expected_issues)

    if score >= 1.0:
        score = 0.99
    elif score <= 0.0:
        score = 0.01

    return score
