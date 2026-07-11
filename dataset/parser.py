import json
from pathlib import Path
from typing import List
from schemas import Entity, Document

class LegalDatasetParser:
    def __init__(self):
        pass

    def parser_file(self, file_path : str) -> List[Document] :
        with open(file_path, "r", encoding = "utf-8") as file:
            data = json.load(file)

            documents = []
            for sample in data:
                document_id = sample['id']
                text = sample['data']['text']

                entities = []
                results = sample['annotations'][0]['result']
                for result in results :
                    value = result['value']
                    entity = Entity(start = value['start'], end = value['end'], text = value['text'], label = value['labels'][0])
                entities.append(entity)
                documents.append(Document(document_id = document_id, text = text, entities = entities))
        return documents
    

    def parse_directory(self, directory : str) -> List[Document] :
        json_files = sorted(Path(directory).glob("*.json"))
        documents = []
        for file in json_files:
            docs = self.parser_file(file)
            documents.extend(docs)
            return documents