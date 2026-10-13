import spacy

nlp = spacy.load("en_core_web_sm")

text = "Part-of-speech tagging labels words by their grammar."
doc = nlp(text)

print("\nPOS Tagging using Neural Model(SpaCy):")
for token in doc:
    print(f"{token.text}->{token.pos_}({token.tag_})")
