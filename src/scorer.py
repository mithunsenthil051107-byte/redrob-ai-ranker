def calculate_score(features, jd):
    score = 0

    # Semantic Similarity (temporarily disabled)
    profile_text = (
        features["current_title"] + " " +
        " ".join(features["skills"]) + " " +
        " ".join(features["career_descriptions"])
    )

    similarity = 0.0
    score += 0

    # Skill Match (25 marks)
    candidate_skills = [s.lower() for s in features["skills"]]
    jd_skills = [s.lower() for s in jd["required_skills"]]

    matched = len(set(candidate_skills) & set(jd_skills))

    if len(jd_skills) > 0:
        score += (matched / len(jd_skills)) * 25

    # Experience (15 marks)
    years = features["years_of_experience"]
    score += min(years / 10, 1) * 15

    # Profile Completeness (10 marks)
    score += (features["profile_score"] / 100) * 10

    # Recruiter Response Rate (10 marks)
    score += features["response_rate"] * 10

    reasoning = (
        f"{features['current_title']} | "
        f"{years:.1f} yrs | "
        f"{matched} JD skills matched | "
        f"Similarity {similarity:.2f}"
    )

    return round(score, 2), reasoning