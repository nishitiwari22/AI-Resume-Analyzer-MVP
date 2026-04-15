from sklearn.linear_model import LogisticRegression
from app.model import get_embedding
from app.utils import clean_text
from data.evaluation_data import data

X = []
y = []

for resume, jd, label in data:
    emb1 = get_embedding(clean_text(resume))
    emb2 = get_embedding(clean_text(jd))

    combined = emb1 - emb2   # feature difference
    X.append(combined)
    y.append(label)

model = LogisticRegression()
model.fit(X, y)