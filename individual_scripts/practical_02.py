import pandas as pd

df = pd.read_csv("annual-enterprise-survey-2025-financial-year-provisional.csv")
print(df.head())
print("Original Dataset:")
print(df)

df = df.dropna()
df = df.drop_duplicates()

print("\n Cleaned Dataset:")
print(df)
df.to_csv("student_cleaned.csv", index=False)
print("\n Blank values and duplicate rows removed successfully.")
