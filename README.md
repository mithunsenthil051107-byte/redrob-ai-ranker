
# AI Candidate Ranking System

## Overview

An AI-powered candidate ranking system developed for the Redrob AI Engineer Hiring Challenge.

The application automatically:

* Loads candidate profiles
* Parses a job description
* Extracts structured features
* Scores candidates using AI-inspired ranking logic
* Generates a ranked submission CSV



## Features

* Candidate data loader
* Job description parser
* Feature engineering
* Candidate scoring engine
* Ranking pipeline
* Automatic CSV generation


## Project Structure

```
src/
    loader.py
    feature_engineering.py
    jd_parser.py
    scorer.py
    ranker.py
    embeddings.py
```



## Installation

```bash
pip install -r requirements.txt
```



## Run

```bash
python main.py
```

Generated file:

```
output/submission.csv
```


## Technologies

* Python
* Pandas
* Scikit-Learn
* Python-Docx


## Future Improvements

* Sentence Transformer embeddings
* Better semantic matching
* Streamlit dashboard
* Explainable AI ranking
* LLM-powered candidate reasoning


## Author

Mithun Senthil

# AI Candidate Ranking System

## Team

This project was developed by **Team CipherNova** as part of the **Redrob AI Hiring Challenge**.

### Team Members

* Mithun Senthil
* KOVARSHINI R V 
* HARISH C J


## Repository

GitHub Repository:
https://github.com/mithunsenthil051107-byte/redrob-ai-ranker

An AI-powered candidate ranking system developed as part of the Redrob AI Hiring Challenge.

## Overview

This project automatically ranks candidates for a job description by extracting candidate information, engineering useful features, and computing a ranking score.

The system:

* Loads candidate profiles from a JSONL dataset
* Parses a job description from a DOCX file
* Extracts important candidate features
* Scores candidates based on skills, experience, and profile quality
* Generates a ranked CSV file for submission


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


## Features

* Candidate data loading
* Job description parsing
* Feature engineering
* Candidate scoring
* Candidate ranking
* Submission CSV generation



## Technologies Used

* Python
* Pandas
* Scikit-learn
* python-docx
* Git
* GitHub



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


## Output

The ranked candidates are saved as:

```text
output/submission.xlsx
```



## Future Improvements

* Semantic matching using Sentence Transformers
* Streamlit web interface
* Improved AI-based ranking model
* Explainable AI scoring
* Dashboard for recruiters



GitHub: https://github.com/mithunsenthil051107-byte

