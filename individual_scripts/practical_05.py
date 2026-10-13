import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

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
