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
