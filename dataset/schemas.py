from dataclasses import dataclass
from typing import List

@dataclass(slots=True)
class Entity:
    start : int
    end : int
    text : str
    label : str

    
@dataclass(slots=True)
class Document:
    document_id : str
    text : str
    entities : List[Entity]