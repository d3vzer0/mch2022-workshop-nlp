from spacy import displacy
import spacy

# Load the prebuilt spacy model (lg)
nlp = spacy.load("en_core_web_lg")

# Open sample text file
with open('sampletext.txt', 'r') as inputfile:
    text = inputfile.read()

# Input text into spacy nlp object
doc = nlp(text)

# Show results
spacy.displacy.serve(doc, style="dep")
