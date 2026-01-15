import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../data/student_scores.csv")

# Feature Engineering
df["avg_score"] = df[["score_easy", "score_medium", "score_hard"]].mean(axis=1)
df["score_variance"] = df[["score_easy", "score_medium", "score_hard"]].var(axis=1)

print("After Feature Engineering:\n")
print(df)
