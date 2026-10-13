"""
Natural Language Processing (NLP) — Practical Journal
Student Name: Mohammed Emad Nadeem Shaikh
Class: TY Data Science | Roll No: 48 | Student ID: 5181765
"""

def practical_1():
    print("\n--- Practical 1: Sentence Segmentation & Word Tokenization ---")
    import nltk
    from nltk.tokenize import sent_tokenize, word_tokenize

    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)

    text = "Natural Language Processing (NLP) is a branch of artificial intelligence. It helps computers read, understand, and write human language."
    sentences = sent_tokenize(text)
    print("Sentence Segmentation:")
    for idx, sentence in enumerate(sentences, 1):
        print(f"Sentence {idx}:{sentence}")

    print("\nWord Tokenization:")
    for idx, sentence in enumerate(sentences, 1):
        tokens = word_tokenize(sentence)
        print(f"Sentence{idx}: {tokens}")


def practical_2():
    print("\n--- Practical 2: Dataset Cleaning with Pandas ---")
    import pandas as pd
    try:
        df = pd.read_csv("annual-enterprise-survey-2025-financial-year-provisional.csv")
    except FileNotFoundError:
        print("Dataset file not found in current directory.")
        return

    print("First 5 rows:")
    print(df.head())

    print("\nOriginal Dataset:")
    print(df)

    df = df.dropna()
    df = df.drop_duplicates()

    print("\nCleaned Dataset:")
    print(df)

    df.to_csv("student_cleaned.csv", index=False)
    print("\nBlank values and duplicate rows removed successfully.")


def practical_3():
    print("\n--- Practical 3: Stemming and Lemmatization ---")
    import nltk
    from nltk.stem import PorterStemmer, WordNetLemmatizer
    from nltk.tokenize import word_tokenize

    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)

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


def practical_4():
    print("\n--- Practical 4: POS Tagging with NLTK ---")
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk import pos_tag

    nltk.download('punkt_tab', quiet=True)
    nltk.download('averaged_perceptron_tagger_eng', quiet=True)

    text = input("Enter a sentence: ")
    words = word_tokenize(text)
    tags = pos_tag(words)

    print("\nPOS Tags:")
    for word, tag in tags:
        print(f"{word}--> {tag}")


def practical_5():
    print("\n--- Practical 5: Counting POS Tags ---")
    import nltk
    from nltk.tokenize import word_tokenize
    from collections import Counter

    nltk.download('punkt', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)

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


def practical_6():
    print("\n--- Practical 6: Trigram Generation and Frequency ---")
    import nltk
    from nltk.util import ngrams
    from nltk.tokenize import word_tokenize
    from collections import Counter

    nltk.download('punkt', quiet=True)

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


def practical_7():
    print("\n--- Practical 7: POS Tagging with SpaCy ---")
    import spacy
    nlp = spacy.load("en_core_web_sm")

    text = "Part-of-speech tagging labels words by their grammar."
    doc = nlp(text)
    print("\nPOS Tagging using Neural Model(SpaCy):")
    for token in doc:
        print(f"{token.text}->{token.pos_}({token.tag_})")


def practical_8():
    print("\n--- Practical 8: Named Entity Recognition (NER) with SpaCy ---")
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


def practical_9():
    print("\n--- Practical 9: Spell Checking with SpellChecker ---")
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


def practical_10():
    print("\n--- Practical 10: TF-IDF Vectorization ---")
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


def practical_11():
    print("\n--- Practical 11: Text Classification with Naive Bayes ---")
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


if __name__ == "__main__":
    practicals = {
        1: practical_1,
        2: practical_2,
        3: practical_3,
        4: practical_4,
        5: practical_5,
        6: practical_6,
        7: practical_7,
        8: practical_8,
        9: practical_9,
        10: practical_10,
        11: practical_11
    }

    print("=== NLP Practicals (Sem 5) ===")
    print("Select a practical to run (1-11):")
    for num in practicals:
        print(f"  {num}. Practical {num}")
    
    try:
        choice = int(input("\nEnter choice: "))
        if choice in practicals:
            practicals[choice]()
        else:
            print("Invalid choice!")
    except Exception as e:
        print(f"Error: {e}")
