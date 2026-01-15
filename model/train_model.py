import pandas as pd
import os
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# ---------- Path Handling ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "student_scores.csv")

# ---------- Load Data ----------
df = pd.read_csv(csv_path)

# ---------- Feature Engineering ----------
df["avg_score"] = df[["score_easy", "score_medium", "score_hard"]].mean(axis=1)
df["score_variance"] = df[["score_easy", "score_medium", "score_hard"]].var(axis=1, ddof=0)

def assign_label(row):
    if row["avg_score"] >= 80 and row["score_variance"] < 50:
        return "Strong"
    elif (
        row["avg_score"] >= 80
        and row["score_variance"] >= 50
        and row["time_taken"] >= 180
    ):
        return "Memorized"
    else:
        return "Fragile"


df["label"] = df.apply(assign_label, axis=1)

# ---------- Prepare ML Data ----------
X = df[["avg_score", "score_variance", "time_taken"]]
y = df["label"]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# ---------- Train Model ----------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X, y_encoded)

# ---------- Save Model ----------
model_path = os.path.join(BASE_DIR, "model", "fragility_model.pkl")
with open(model_path, "wb") as f:
    pickle.dump((model, encoder), f)

print("✅ Model trained and saved successfully!")
