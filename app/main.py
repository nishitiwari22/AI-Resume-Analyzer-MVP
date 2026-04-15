from fastapi import FastAPI
from pydantic import BaseModel

from app.utils import clean_text, extract_skills, skill_gap
from app.model import get_embedding, compute_similarity
from app.classifier import predict_match

app = FastAPI()


# -----------------------------
# Request Schema
# -----------------------------
class AnalyzeRequest(BaseModel):
    resume: str
    jd: str


# -----------------------------
# Helper Function
# -----------------------------
def generate_feedback(score, missing_skills):
    if score > 75:
        level = "Good Match"
    elif score > 50:
        level = "Moderate Match"
    else:
        level = "Low Match"

    if missing_skills:
        suggestion = f"Improve your resume by adding: {', '.join(missing_skills)}"
    else:
        suggestion = "Your resume matches well with the job description"

    return level, suggestion


# -----------------------------
# Analyze Endpoint
# -----------------------------
@app.post("/analyze")
def analyze(data: AnalyzeRequest):
    # Extract input
    resume = data.resume
    jd = data.jd

    # Clean text
    resume_clean = clean_text(resume)
    jd_clean = clean_text(jd)

    # Generate embeddings
    resume_emb = get_embedding(resume_clean)
    jd_emb = get_embedding(jd_clean)

    # Compute similarity score
    score = compute_similarity(resume_emb, jd_emb)

    # Extract skills
    resume_skills = extract_skills(resume_clean)
    jd_skills = extract_skills(jd_clean)

    # Find missing skills
    missing = skill_gap(resume_skills, jd_skills)

    # Generate feedback
    level, suggestion = generate_feedback(score, missing)

    return {
        "match_score": score,
        "match_level": level,
        "missing_skills": missing,
        "suggestion": suggestion
    }


# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
def predict(data: AnalyzeRequest):
    prediction = predict_match(data.resume, data.jd)

    return {
        "prediction": "Match" if prediction == 1 else "Not a Match"
    }