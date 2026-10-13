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
