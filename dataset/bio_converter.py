from typing import List, Tuple
from schemas import Document,Token
from word_tokenizer import WordTokenizer


class BIOConverter:
    def convert(self, document : Document) -> Tuple[List[str], List[str]] :
        doc = nlp(document.text)
        labels = ["O"] * len(doc)
        for entity in document.entities :
            for token_index, token in enumerate(doc):
                token_start = token.idx
                token_end = token.idx + len(token)
                if (token_start >= entity.start  and token_end <= entity.end):
                    if token_start == entity.start :
                        labels[token_index] = (f"B-{entity.label}")
                    else:
                        labels[token_index] = (f"I-{entity.label}")
        tokens = [token.text for token in doc]
        return tokens, labels
