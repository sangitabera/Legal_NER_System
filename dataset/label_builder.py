""" 
builds BIO label mappings automatically from the dataset
"""

import json
from pathlib import Path
from typing import Dict, List, Set

from configs.config import config
from configs.constants import (
    OUTSIDE_TAG,
    B_PREFIX,
    I_PREFIX,
)
from configs.logging_config import get_logger
from dataset.schemas import Document

logger = get_logger(__name__)


class LabelBuilder:

    def __init__(self):

        self.label2id: Dict[str, int] = {}

        self.id2label: Dict[int, str] = {}

    def collect_labels(
        self,
        documents: List[Document]
    ) -> Set[str]:

        labels = set()

        for document in documents:

            for entity in document.entities:

                labels.add(entity.label)

        return labels

    def build(
        self,
        documents: List[Document]
    ):

        labels = sorted(
            self.collect_labels(documents)
        )

        bio_labels = [OUTSIDE_TAG]

        for label in labels:

            bio_labels.append(
                f"{B_PREFIX}-{label}"
            )

            bio_labels.append(
                f"{I_PREFIX}-{label}"
            )

        self.label2id = {

            label: idx

            for idx, label

            in enumerate(bio_labels)

        }

        self.id2label = {

            idx: label

            for label, idx

            in self.label2id.items()

        }

        logger.info(
            "Discovered %d BIO labels.",
            len(self.label2id)
        )

    def save(self):

        output_dir = config.data.PROCESSED_DIR

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        output_file = output_dir / "label_map.json"

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {
                    "label2id": self.label2id,
                    "id2label": self.id2label
                },
                file,
                indent=4
            )

        logger.info(
            "Saved label map to %s",
            output_file
        )