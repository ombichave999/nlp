# Natural Language Processing (NLP) — Practical Journal (Sem 5)

> **Name:** Mohammed Emad Nadeem Shaikh  
> **Class:** TY Data Science | **Roll No:** 48 | **Student ID:** 5181765  
> **Subject:** Natural Language Processing (NLP)

---

## 📌 Quick Practical Index

Click any practical to jump directly to its Aim, Code, and Output:

* [Practical 1: Sentence Segmentation & Word Tokenization (NLTK)](#practical-1)
* [Practical 2: Data Cleaning — Missing Values & Duplicates (Pandas)](#practical-2)
* [Practical 3: Stemming & Lemmatization (NLTK)](#practical-3)
* [Practical 4: Part-of-Speech (POS) Tagging (NLTK)](#practical-4)
* [Practical 5: Counting Part-of-Speech (POS) Tags (NLTK)](#practical-5)
* [Practical 6: Generation of Trigrams & Frequency Count (NLTK)](#practical-6)
* [Practical 7: POS Tagging using Neural Language Model (SpaCy)](#practical-7)
* [Practical 8: Named Entity Recognition — NER (SpaCy)](#practical-8)
* [Practical 9: Spelling Check & Correction (SpellChecker)](#practical-9)
* [Practical 10: TF-IDF Vectorization (Scikit-Learn)](#practical-10)
* [Practical 11: Text Classification using Naive Bayes (Scikit-Learn)](#practical-11)

---

### ⚙️ Quick Installation (Run in College Terminal if packages are missing)
```bash
pip install nltk spacy pyspellchecker scikit-learn pandas
python -m spacy download en_core_web_sm
```

---

<a id="practical-1"></a>
## PRACTICAL 1

**Aim:**  
To perform sentence segmentation and word tokenization on a given text using the NLTK library.

```python
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download tokenizer models (run once)
nltk.download('punkt')
nltk.download('punkt_tab')

text = "Natural Language Processing (NLP) is a branch of artificial intelligence. It helps computers read, understand, and write human language."

# Sentence segmentation
sentences = sent_tokenize(text)
print("Sentence Segmentation:")
for idx, sentence in enumerate(sentences, 1):
    print(f"Sentence {idx}:{sentence}")

# Word tokenization
print("\nWord Tokenization:")
for idx, sentence in enumerate(sentences, 1):
    tokens = word_tokenize(sentence)
    print(f"Sentence{idx}: {tokens}")
```

#### Output:
```text
Sentence Segmentation:
Sentence 1:Natural Language Processing (NLP) is a branch of artificial intelligence.
Sentence 2:It helps computers read, understand, and write human language.

Word Tokenization:
Sentence1: ['Natural', 'Language', 'Processing', '(', 'NLP', ')', 'is', 'a', 'branch', 'of', 'artificial', 'intelligence', '.']
Sentence2: ['It', 'helps', 'computers', 'read', ',', 'understand', ',', 'and', 'write', 'human', 'language', '.']
```

---

<a id="practical-2"></a>
## PRACTICAL 2

**Aim:**  
To clean a dataset by removing missing values and duplicate records using Pandas.

```python
import pandas as pd

# Read dataset
df = pd.read_csv("annual-enterprise-survey-2025-financial-year-provisional.csv")
print("First 5 rows:")
print(df.head())

print("\nOriginal Dataset:")
print(df)

# Drop missing and duplicate rows
df = df.dropna()
df = df.drop_duplicates()

print("\nCleaned Dataset:")
print(df)

# Save cleaned output
df.to_csv("student_cleaned.csv", index=False)
print("\nBlank values and duplicate rows removed successfully.")
```

#### Output:
```text
Cleaned Dataset:
[60255 rows x 10 columns]

Blank values and duplicate rows removed successfully.
```

---

<a id="practical-3"></a>
## PRACTICAL 3

**Aim:**  
To perform Stemming and Lemmatization on a given sentence using the NLTK library in python.

```python
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download wordnet resources
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

print("\nLemmatization:")
for word in tokens:
    print(f"{word}->{lemmatizer.lemmatize(word)}")
```

#### Output:
```text
stemming:
Do->do
what->what
you->you
can->can
,->,
with->with
what->what
you->you
have->have
,->,
where->where
you->you
are->are

Lemmatization:
Do->Do
what->what
you->you
can->can
,->,
with->with
what->what
you->you
have->have
,->,
where->where
you->you
are->are
```

---

<a id="practical-4"></a>
## PRACTICAL 4

**Aim:**  
Part-of-speech (POS) tagging using NLTK.

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources (run only once)
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = input("Enter a sentence: ")

# Tokenize
words = word_tokenize(text)

# POS tagging
tags = pos_tag(words)

print("\nPOS Tags:")
for word, tag in tags:
    print(f"{word}--> {tag}")
```

#### Sample Run:
* **Input:** `If you tell the truth, you do not have to remember anything`
* **Output:**
```text
POS Tags:
If--> IN
you--> PRP
tell--> VBP
the--> DT
truth--> NN
,--> ,
you--> PRP
do--> VBP
not--> RB
have--> VB
to--> TO
remember--> VB
anything--> NN
```

---

<a id="practical-5"></a>
## PRACTICAL 5

**Aim:**  
Counting Part-of-speech (POS) tags using NLTK.

```python
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Download resources (Run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input sentence
text = "If you tell the truth, you don't have to remember anything"

# Tokenization
tokens = word_tokenize(text)

# POS Tagging
pos_tags = nltk.pos_tag(tokens)

# Display POS Tags
print("POS Tags:")
print(pos_tags)

# Count POS Tags
tags = [tag for word, tag in pos_tags]
tag_count = Counter(tags)

print("\nCount of POS Tags:")
for tag, count in tag_count.items():
    print(f"{tag}:{count}")
```

#### Output:
```text
POS Tags:
[('If', 'IN'), ('you', 'PRP'), ('tell', 'VBP'), ('the', 'DT'), ('truth', 'NN'), (',', ','), ('you', 'PRP'), ('do', 'VBP'), ("n't", 'RB'), ('have', 'VB'), ('to', 'TO'), ('remember', 'VB'), ('anything', 'NN')]

Count of POS Tags:
IN:1
PRP:2
VBP:2
DT:1
NN:2
,:1
RB:1
VB:2
TO:1
```

---

<a id="practical-6"></a>
## PRACTICAL 6

**Aim:**  
Generation of trigrams and frequency count using NLTK.

```python
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

# Download resources if not already done
nltk.download('punkt')

# Input text
text = "NLP helps computers understand human language."

# Tokenize and convert to lowercase
tokens = word_tokenize(text.lower())

# Generate trigrams
trigrams = list(ngrams(tokens, 3))

# Display the trigrams
print("Generated trigrams:")
for trigram in trigrams:
    print(trigram)

# Frequency count
trigram_freq = Counter(trigrams)
print("\nTrigram Frequencies:")
for trigram, freq in trigram_freq.items():
    print(f"{trigram} : {freq}")
```

#### Output:
```text
Generated trigrams:
('nlp', 'helps', 'computers')
('helps', 'computers', 'understand')
('computers', 'understand', 'human')
('understand', 'human', 'language')
('human', 'language', '.')

Trigram Frequencies:
('nlp', 'helps', 'computers') : 1
('helps', 'computers', 'understand') : 1
('computers', 'understand', 'human') : 1
('understand', 'human', 'language') : 1
('human', 'language', '.') : 1
```

---

<a id="practical-7"></a>
## PRACTICAL 7

**Aim:**  
Part-of-speech (POS) tagging using SpaCy neural language model.

```python
import spacy

# Load English model (neural network-based)
nlp = spacy.load("en_core_web_sm")

# Input sentence
text = "Part-of-speech tagging labels words by their grammar."

# Process the text
doc = nlp(text)
print("\nPOS Tagging using Neural Model(SpaCy):")
for token in doc:
    print(f"{token.text}->{token.pos_}({token.tag_})")
```

#### Output:
```text
POS Tagging using Neural Model(SpaCy):
Part->NOUN(NN)
-->PUNCT(HYPH)
of->ADP(IN)
-->PUNCT(HYPH)
speech->NOUN(NN)
tagging->VERB(VBG)
labels->VERB(VBZ)
words->NOUN(NNS)
by->ADP(IN)
their->PRON(PRP$)
grammar->NOUN(NN)
.->PUNCT(.)
```

---

<a id="practical-8"></a>
## PRACTICAL 8

**Aim:**  
To perform Named Entity Recognition (NER) on a given sentence using SpaCy to identify entities such as persons, organizations, locations and dates.

```python
import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# User input
text = input("Enter a sentence: ")

# Process the text
doc = nlp(text)

# Check whether any named entities are found
if len(doc.ents) == 0:
    print("\nNo Named Entity Found.")
    print("Please enter a sentence containing a person's name, organization, place, date, etc.")
else:
    print("\nNamed Entities Found:\n")
    for ent in doc.ents:
        print(f"{ent.text}->{ent.label_}")
```

#### Sample Run:
* **Input:** `Qin Shi Huang (February 259 - 12 July 210 BC) was the founder of the Qin dynasty and the first emperor of China`
* **Output:**
```text
Named Entities Found:

Qin Shi Huang->PERSON
February 259->DATE
12 July->DATE
BC->ORG
Qin->PERSON
first->ORDINAL
China->GPE
```

---

<a id="practical-9"></a>
## PRACTICAL 9

**Aim:**  
To implement spell checking for English text by identifying and correcting misspelled words using the Spellchecker library in Python.

```python
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
```

#### Sample Run:
* **Input:** `I stduy data sciencee`
* **Output:**
```text
Original Sentence:
I stduy data sciencee

Corrected Sentence:
I study data science
```

---

<a id="practical-10"></a>
## PRACTICAL 10

**Aim:**  
To implement TF-IDF (Term Frequency–Inverse Document Frequency) vectorization using the Scikit-learn library in Python and convert text documents into numerical feature vectors.

```python
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
```

#### Output:
```text
Feature Names:
['algorithms' 'amounts' 'and' 'based' 'data' 'decisions' 'everyday'
 'evidence' 'extracts' 'faster' 'from' 'helps' 'insights' 'it' 'like'
 'make' 'massive' 'more' 'of' 'organizations' 'powers' 'predictive'
 'science' 'smarter' 'technology' 'valuable']

TF-IDF Matrix:
[[0.         0.28867513 0.         0.         0.57735027 0.
  0.         0.         0.28867513 0.         0.28867513 0.
  0.28867513 0.         0.         0.         0.28867513 0.
  0.28867513 0.         0.         0.         0.28867513 0.
  0.         0.28867513]
 [0.38988801 0.         0.         0.         0.         0.
  0.38988801 0.         0.         0.         0.         0.
  0.         0.29651988 0.38988801 0.         0.         0.
  0.         0.         0.38988801 0.38988801 0.         0.
  0.38988801 0.        ]
 [0.         0.         0.30746099 0.30746099 0.         0.30746099
  0.         0.30746099 0.         0.30746099 0.         0.30746099
  0.         0.23383201 0.         0.30746099 0.         0.30746099
  0.         0.30746099 0.         0.         0.         0.30746099
  0.         0.        ]]
```

---

<a id="practical-11"></a>
## PRACTICAL 11

**Aim:**  
To implement text classification using CountVectorizer and the Multinomial Naive Bayes algorithm using the Scikit-learn library in Python.

```python
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
```

#### Sample Run:
* **Input:** `I like cricket`
* **Output:**
```text
Category: Sports
```