from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from app.model import get_embedding, compute_similarity
from app.utils import clean_text
from data.evaluation_data import data

y_true = []
y_pred = []

for resume, jd, label in data:
    resume_emb = get_embedding(clean_text(resume))
    jd_emb = get_embedding(clean_text(jd))

    score = compute_similarity(resume_emb, jd_emb)

    prediction = 1 if score > 50 else 0

    y_true.append(label)
    y_pred.append(prediction)

print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1 Score:", f1_score(y_true, y_pred))