from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

text = [
    "I like cricket",
    "Football is my favorite sport",
    "I watch cricket matches",
    "I like studying computer science",
    "Python is easy to learn",
    "I study mathematics"
]

category = [
    "Sports",
    "Sports",
    "Sports",
    "Education",
    "Education",
    "Education"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)

model = MultinomialNB()
model.fit(X, category)

sentence = input("Enter a sentence: ")
sentence_vector = vectorizer.transform([sentence])

if sentence_vector.nnz == 0:
    print("Not trained for this data")
else:
    result = model.predict(sentence_vector)
    print("Category:", result[0])
