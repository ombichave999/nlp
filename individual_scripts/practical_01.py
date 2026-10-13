import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")

text = "Natural Language Processing (NLP) is a branch of artificial intelligence. It helps computers read, understand, and write human language."

sentences = sent_tokenize(text)
print("Sentence Segmentation:")
for idx, sentence in enumerate(sentences, 1):
    print(f"Sentence {idx}:{sentence}")

print("\nWord Tokenization:")
for idx, sentence in enumerate(sentences, 1):
    tokens = word_tokenize(sentence)
    print(f"Sentence{idx}: {tokens}")
