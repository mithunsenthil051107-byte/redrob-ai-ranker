import pandas as pd

from src.loader import load_candidates
from src.feature_engineering import extract_features
from src.scorer import calculate_score


def rank_candidates(candidate_file, jd):
    results = []

    for candidate in load_candidates(candidate_file):

        features = extract_features(candidate)

        score, reasoning = calculate_score(features, jd)

        results.append({
            "candidate_id": features["candidate_id"],
            "score": score,
            "reasoning": reasoning
        })

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="score",
        ascending=False
    ).reset_index(drop=True)

    df["rank"] = df.index + 1

    return df[
        [
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]
    ]