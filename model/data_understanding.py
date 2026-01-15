import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "student_scores.csv")

df = pd.read_csv(csv_path)

print("Dataset Preview:\n")
print(df)

print("\nStatistics:\n")
print(df.describe())
