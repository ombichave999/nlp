import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

text = input("Enter a sentence: ")
words = word_tokenize(text)
tags = pos_tag(words)

print("\nPOS Tags:")
for word, tag in tags:
    print(f"{word}--> {tag}")
