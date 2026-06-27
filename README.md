# AI Candidate Ranking System

An AI-powered candidate ranking system developed as part of the Redrob AI Hiring Challenge.

## Overview

This project automatically ranks candidates for a job description by extracting candidate information, engineering useful features, and computing a ranking score.

The system:

* Loads candidate profiles from a JSONL dataset
* Parses a job description from a DOCX file
* Extracts important candidate features
* Scores candidates based on skills, experience, and profile quality
* Generates a ranked CSV file for submission

---

## Project Structure

```text
redrob-ai-ranker/
│
├── data/
│   ├── candidates.jsonl
│   ├── job_description.docx
│   └── sample_submission.csv
│
├── output/
│   └── submission.csv
│
├── src/
│   ├── loader.py
│   ├── feature_engineering.py
│   ├── jd_parser.py
│   ├── scorer.py
│   ├── ranker.py
│   ├── embeddings.py
│   └── explain.py
│
├── main.py
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Features

* Candidate data loading
* Job description parsing
* Feature engineering
* Candidate scoring
* Candidate ranking
* Submission CSV generation

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* python-docx
* Git
* GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mithunsenthil051107-byte/redrob-ai-ranker.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## Output

The ranked candidates are saved as:

```text
output/submission.csv
```

---

## Future Improvements

* Semantic matching using Sentence Transformers
* Streamlit web interface
* Improved AI-based ranking model
* Explainable AI scoring
* Dashboard for recruiters

---

## Author

**Mithun Senthil**

GitHub: https://github.com/mithunsenthil051107-byte
