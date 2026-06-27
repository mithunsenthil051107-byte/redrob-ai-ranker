# AI Candidate Ranking System

## Overview

An AI-powered candidate ranking system developed for the Redrob AI Engineer Hiring Challenge.

The application automatically:

* Loads candidate profiles
* Parses a job description
* Extracts structured features
* Scores candidates using AI-inspired ranking logic
* Generates a ranked submission CSV

---

## Features

* Candidate data loader
* Job description parser
* Feature engineering
* Candidate scoring engine
* Ranking pipeline
* Automatic CSV generation

---

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

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

Generated file:

```
output/submission.csv
```

---

## Technologies

* Python
* Pandas
* Scikit-Learn
* Python-Docx

---

## Future Improvements

* Sentence Transformer embeddings
* Better semantic matching
* Streamlit dashboard
* Explainable AI ranking
* LLM-powered candidate reasoning

---

## Author

Mithun Senthil
