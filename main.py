from src.jd_parser import parse_job_description
from src.ranker import rank_candidates

jd = parse_job_description("data/job_description.docx")

df = rank_candidates(
    "data/candidates.jsonl",
    jd
)

print(df.head(10))

df.to_csv(
    "output/submission.csv",
    index=False
)

print("\nSubmission saved to output/submission.csv")