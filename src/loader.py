import json

def load_candidates(file_path):
    """
    Reads the candidates.jsonl file one candidate at a time.
    This is memory efficient for large datasets.
    """

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:

            if line.strip():

                yield json.loads(line)