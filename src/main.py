"""
This is the main entry point for the application.
It loads the trained model and tests it on a sample input.
"""

import spacy

if __name__ == "__main__":
    nlp = spacy.load("./output/model-best")
    doc = nlp("Set an alarm for 7 am tomorrow")
    for ent in doc.ents:
        print(ent.text, ent.label_)
