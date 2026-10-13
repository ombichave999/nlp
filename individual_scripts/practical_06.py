import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download("punkt")

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
