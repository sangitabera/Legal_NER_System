from .schemas import Document, ValidationResult
from configs.logging_config import get_logger

logger = get_logger(__name__)

class DatasetValidator:
    def validate(self, document: Document) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        if not document.text.strip():
            result.errors.append(
                "document text is empty."
            )
        
        for entity in document.entities:
            if entity.start < 0:
                result.is_valid = False
                result.errors.append(
                    "Negative start offset."
                )
            
            if entity.end > len(document.text):
                result.is_valid = False
                result.errors.append(
                    "end offset exceeds document length."
                )
            
            if entity.start >= entity.end:
                result.is_valid = False
                result.errors.append(
                    "invalid entity span."
                )
        
        actual_text = document.text[entity.start : entity.end]
        if actual_text != entity.text:
            result.is_valid = False
            result.errors.append(
                    f"Entity mismatch: "
                    f"'{entity.text}'"
                    f"!= "
                    f"'{actual_text}'"
                )
            
        if result.is_valid:
            logger.info(
                "document validated sucessfully."
            )
        else:
            logger.warning(
                "validation failed."
            )
        return result