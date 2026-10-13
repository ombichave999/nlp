# Natural Language Processing (NLP) Practicals

============================================================
PRACTICAL 1
Aim: To perform sentence segmentation and word tokenization on a given text using the NLTK library.
============================================================
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Natural Language Processing (NLP) is a branch of artificial intelligence. It helps computers read, understand, and write human language."

sentences = sent_tokenize(text)
print("Sentence Segmentation:")
for idx, sentence in enumerate(sentences, 1):
    print(f"Sentence {idx}:{sentence}")

print("\nWord Tokenization:")
for idx, sentence in enumerate(sentences, 1):
    tokens = word_tokenize(sentence)
    print(f"Sentence{idx}: {tokens}")


============================================================
PRACTICAL 2
Aim: To clean a dataset by removing missing values and duplicate records using Pandas.
============================================================
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


============================================================
PRACTICAL 3
Aim: To perform Stemming and Lemmatization on a given sentence using the NLTK library in python.
============================================================
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = "Do what you can, with what you have, where you are"
tokens = word_tokenize(text)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("stemming:")
for word in tokens:
    print(f"{word}->{stemmer.stem(word)}")

print("\n Lemmatization:")
for word in tokens:
    print(f"{word}->{lemmatizer.lemmatize(word)}")


============================================================
PRACTICAL 4
Aim: Part-of-speech (POS) tagging using NLTK.
============================================================
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = input("Enter a sentence: ")

words = word_tokenize(text)
tags = pos_tag(words)

print("\nPOS Tags:")
for word, tag in tags:
    print(f"{word}--> {tag}")


============================================================
PRACTICAL 5
Aim: Counting Part-of-speech (POS) tags using NLTK.
============================================================
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "If you tell the truth, you don't have to remember anything"

tokens = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)

print("POS Tags:")
print(pos_tags)

tags = [tag for word, tag in pos_tags]
tag_count = Counter(tags)

print("\nCount of POS Tags:")
for tag, count in tag_count.items():
    print(f"{tag}:{count}")


============================================================
PRACTICAL 6
Aim: Generation of trigrams and frequency count using NLTK.
============================================================
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')

text = "NLP helps computers understand human language."
tokens = word_tokenize(text.lower())
trigrams = list(ngrams(tokens, 3))

print("Generated trigrams:")
for trigram in trigrams:
    print(trigram)

trigram_freq = Counter(trigrams)
print("\nTrigram Frequencies:")
for trigram, freq in trigram_freq.items():
    print(f"{trigram} : {freq}")


============================================================
PRACTICAL 7
Aim: Part-of-speech (POS) tagging using SpaCy neural language model.
============================================================
import spacy

nlp = spacy.load("en_core_web_sm")

text = "Part-of-speech tagging labels words by their grammar."
doc = nlp(text)

print("\nPOS Tagging using Neural Model(SpaCy):")
for token in doc:
    print(f"{token.text}->{token.pos_}({token.tag_})")


============================================================
PRACTICAL 8
Aim: To perform Named Entity Recognition (NER) on a given sentence using SpaCy to identify entities such as persons, organizations, locations and dates.
============================================================
import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a sentence: ")
doc = nlp(text)

if len(doc.ents) == 0:
    print("\nNo Named Entity Found.")
    print("Please enter a sentence containing a person's name, organization, place, date, etc.")
else:
    print("\nNamed Entities Found:\n")
    for ent in doc.ents:
        print(f"{ent.text}->{ent.label_}")


============================================================
PRACTICAL 9
Aim: To implement spell checking for English text by identifying and correcting misspelled words using the Spellchecker library in Python.
============================================================
from spellchecker import SpellChecker

spell = SpellChecker()
sentence = input("Enter a sentence: ")
words = sentence.split()
corrected = []

for word in words:
    corrected.append(spell.correction(word))

print("\nOriginal Sentence:")
print(sentence)
print("\nCorrected Sentence:")
print(" ".join(corrected))


============================================================
PRACTICAL 10
Aim: To implement TF-IDF (Term Frequency–Inverse Document Frequency) vectorization using the Scikit-learn library in Python and convert text documents into numerical feature vectors.
============================================================
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


============================================================
PRACTICAL 11
Aim: To implement text classification using CountVectorizer and the Multinomial Naive Bayes algorithm using the Scikit-learn library in Python.
============================================================
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