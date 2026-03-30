# About
Ana AI is a virtual assistant inspired by Alexa, designed to interact naturally with users, answer questions, and automate daily tasks. It strives to be helpful, fast, and context-aware, providing a smart and friendly experience in every interaction.

# How to train

To train Ana AI, you can follow these steps:

Generate the training and validation data by running the following command:

```bash
python src/generate_data.py
```

Then run the following command to start the training process:

```bash
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy
```

To test the trained model, run the following command:

```bash
python src/main.py
```

# References

- [How to Build a Named Entity Recognition Pipeline with spaCy and Transformers](https://agentbus.sh/posts/how-to-build-a-named-entity-recognition-pipeline/)