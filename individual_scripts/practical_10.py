from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Data science extracts valuable insights from massive amounts of data",
    "It powers everyday technology like predictive algorithms.",
    "By turning raw data into actionable strategies, it helps organizations make smarter, faster, and more evidence-based decisions."
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print("Feature Names:")
print(vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
