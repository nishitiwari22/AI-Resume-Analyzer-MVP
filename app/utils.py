import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

SKILLS = ["python", "sql", "machine learning", "data analysis", "deep learning"]

def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill in text.lower():
            found.append(skill)
    return found


def skill_gap(resume_skills, jd_skills):
    missing = list(set(jd_skills) - set(resume_skills))
    return missing

print("UTILS FILE LOADED")


def extract_skills(text):
    words = text.lower().split()
    return list(set(words) & set(SKILLS))

SKILL_WEIGHTS = {
    "python": 3,
    "sql": 3,
    "machine learning": 5,
    "data analysis": 4,
    "deep learning": 5
}


def weighted_score(resume_skills, jd_skills):
    score = 0
    total = 0

    for skill in jd_skills:
        weight = SKILL_WEIGHTS.get(skill, 1)
        total += weight
        if skill in resume_skills:
            score += weight

    return round((score / total) * 100, 2) if total else 0


def calculate_final_score(similarity_score, skill_score):
    final_score = (0.7 * similarity_score) + (0.3 * skill_score)
    explanation = f"Your resume matches {final_score}% based on semantic similarity and skill overlap"
    return final_score, explanation