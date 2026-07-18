from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataConfig:
    """Dataset paths."""

    RAW_DATA_DIR: Path = Path("data/raw")
    TRAIN_DIR: Path = RAW_DATA_DIR / "train"
    DEV_DIR: Path = RAW_DATA_DIR / "dev"
    TEST_DIR: Path = RAW_DATA_DIR / "test"

    PROCESSED_DIR: Path = Path("data/processed")
    TOKENIZER_DIR: Path = Path("data/tokenizer")
    CACHE_DIR: Path = Path("data/cache")


@dataclass(frozen=True)
class TokenizerConfig:
    """Tokenizer configuration."""

    VOCAB_SIZE: int = 30000
    MIN_FREQUENCY: int = 2

    PAD_TOKEN: str = "[PAD]"
    UNK_TOKEN: str = "[UNK]"
    CLS_TOKEN: str = "[CLS]"
    SEP_TOKEN: str = "[SEP]"
    MASK_TOKEN: str = "[MASK]"


@dataclass(frozen=True)
class ModelConfig:
    """BERT model configuration."""

    HIDDEN_SIZE: int = 768
    NUM_HEADS: int = 12
    NUM_LAYERS: int = 12
    INTERMEDIATE_SIZE: int = 3072
    MAX_POSITION_EMBEDDINGS: int = 512
    DROPOUT: float = 0.1


@dataclass(frozen=True)
class TrainingConfig:
    """Training configuration."""

    BATCH_SIZE: int = 16
    LEARNING_RATE: float = 3e-5
    EPOCHS: int = 10
    WEIGHT_DECAY: float = 0.01
    MAX_GRAD_NORM: float = 1.0
    RANDOM_SEED: int = 42


@dataclass(frozen=True)
class CheckpointConfig:
    """Model saving."""

    SAVE_DIR: Path = Path("checkpoints")
    BEST_MODEL: str = "best_model.pt"
    LAST_MODEL: str = "last_model.pt"


@dataclass(frozen=True)
class Config:
    """Master configuration object."""

    data = DataConfig()
    tokenizer = TokenizerConfig()
    model = ModelConfig()
    training = TrainingConfig()
    checkpoint = CheckpointConfig()

config = Config()