from typing import List, Tuple


def read_conll_file(file_path: str) -> Tuple[List[List[str]], List[List[str]]]:
    """
    Reads a CoNLL formatted file.

    Example input:
    John B-PER
    Smith I-PER
    works O
    at O
    Google B-ORG

    Returns:
        sentences = [["John", "Smith", "works", "at", "Google"]]
        labels = [["B-PER", "I-PER", "O", "O", "B-ORG"]]
    """

    sentences = []
    labels = []

    current_sentence = []
    current_labels = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # Empty line means end of sentence
            if line == "":
                if len(current_sentence) > 0:
                    sentences.append(current_sentence)
                    labels.append(current_labels)
                current_sentence = []
                current_labels = []
                continue
            token, label = line.split()

            current_sentence.append(token)
            current_labels.append(label)

    # Handle last sentence if file doesn't end with blank line
    if len(current_sentence) > 0:
        sentences.append(current_sentence)
        labels.append(current_labels)
    return sentences, labels