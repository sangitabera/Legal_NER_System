from typing import List
import spacy
from schemas import Token

nlp = spacy.load("en_core_web_sm", disable = ["parser", "tagger", "ner", "lemmatizer", "attribute_ruler"])

class WordTokenizer:
    def __init__(self):
        self.nlp = nlp

    def tokenize(self, text : str) -> List[Token]:
        doc = self.nlp(text)
        tokens = []

        for token in doc:
            tokens.append(
                Token(
                    text = token.text,
                    start = token.idx,
                    end = token.idx + len(token.text)
                )
            )
        return token