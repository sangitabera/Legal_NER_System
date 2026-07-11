from dataclasses import dataclass
from typing import List

@dataclass
class Entity:
    start : int
    end : int
    text : str
    label : str


@dataclass
class Token:
    text : str
    start : int
    end : int

    
@dataclass
class Document:
    document_id : str
    text : str
    entities : List[Entity]