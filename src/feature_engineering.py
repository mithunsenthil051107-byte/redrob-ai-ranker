def extract_features(candidate):
    """
    Extract useful features from a candidate profile.
    """

    profile = candidate.get("profile", {})
    skills = candidate.get("skills", [])
    education = candidate.get("education", [])
    career = candidate.get("career_history", [])
    signals = candidate.get("redrob_signals", {})

    features = {
        "candidate_id": candidate.get("candidate_id"),
        "years_of_experience": profile.get("years_of_experience", 0),
        "location": profile.get("location", ""),
        "current_title": profile.get("current_title", ""),
        "current_company": profile.get("current_company", ""),
        "skills": [skill["name"] for skill in skills],
        "education": [edu["degree"] for edu in education],
        "career_descriptions": [job["description"] for job in career],
        "open_to_work": signals.get("open_to_work_flag", False),
        "github_score": signals.get("github_activity_score", 0),
        "profile_score": signals.get("profile_completeness_score", 0),
        "response_rate": signals.get("recruiter_response_rate", 0),
        "notice_period": signals.get("notice_period_days", 999),
    }

    return features