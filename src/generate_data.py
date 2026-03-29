"""Main entry point"""

import spacy
from spacy.tokens import DocBin

from datasets.set_alarm import (
    set_alarm_training_dataset,
    set_alarm_validation_dataset,
)

nlp = spacy.blank("en")
db = DocBin()


if __name__ == "__main__":
    TRAIN_DATA = set_alarm_training_dataset()
    VALIDATION_DATA = set_alarm_validation_dataset()

    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annotations["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is None:
                print(
                    f"Skipping entity [{start}:{end}] in "
                    f"'{text}' - misaligned span"
                )
                continue
            ents.append(span)
        doc.ents = ents
        db.add(doc)

    db.to_disk("./train.spacy")

    for text, annotations in VALIDATION_DATA:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annotations["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is None:
                print(
                    f"Skipping entity [{start}:{end}] in "
                    f"'{text}' - misaligned span"
                )
                continue
            ents.append(span)
        doc.ents = ents
        db.add(doc)

    db.to_disk("./dev.spacy")
