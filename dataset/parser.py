import json
from pathlib import Path
from typing import List
from configs.logging_config import get_logger
from schemas import Entity, Document

logger = get_logger(__name__)

class LegalDatasetParser:
    """ 
    Reads label studio json  files and converts them into document objects
    """
    def __init__(self):
        logger.info("initializing LegalDatasetParser")

    def parser_file(self, file_path : str) -> List[Document] :
        with open(file_path, "r", encoding = "utf-8") as file:
            raw_data = json.load(file)
        
            if not isinstance(raw_data,list):
                raise ValueError("Dataset must be a list.")

            documents = []
            for sample in raw_data:
                document_id = sample['id']
                text = sample['data']['text']

                entities = []
                results = sample['annotations'][0]['result']
                for annotation in results :
                    value = annotation['value']

                    entity = Entity(start = value['start'], end = value['end'], text = value['text'], label = value['labels'][0])
                entities.append(entity)
                documents.append(Document(document_id = document_id, text = text, entities = entities))
                logger.info(
                    "loaded documents",
                    len(documents)
                )
        return documents
    

    def parse_directory(self, directory : Path) -> List[Document] :
        json_files = sorted(directory.glob("*.json"))
        all_documents = []
        for file in json_files:
            docs = self.parser_file(file)
            all_documents.extend(docs)
            logger.info("total documents: ", len(all_documents))
            return all_documents