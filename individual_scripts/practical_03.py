import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")

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
