from docx import Document
import re

def parse_job_description(file_path):
    """
    Read the job description and extract important requirements.
    """

    doc = Document(file_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    # Skills we are interested in
    skills = [
        "Python",
        "LLM",
        "RAG",
        "LangChain",
        "Vector Database",
        "Pinecone",
        "FAISS",
        "AWS",
        "Docker",
        "Kubernetes",
        "Machine Learning",
        "AI"
    ]

    found_skills = []

    for skill in skills:
        if re.search(skill, text, re.IGNORECASE):
            found_skills.append(skill)

    return {
        "job_text": text,
        "required_skills": found_skills
    }