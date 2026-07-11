from pathlib import Path
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import BpeTrainer


def train_tokenizer(files, save_path, vocab_size=30000, min_frequency=2):
    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    tokenizer.pre_tokenizer = Whitespace()

    trainer = BpeTrainer(
        vocab_size=vocab_size,
        min_frequency=min_frequency,
        special_tokens=[
            "[PAD]",
            "[UNK]",
            "[CLS]",
            "[SEP]",
            "[MASK]"
        ])

    tokenizer.train(files, trainer)

    Path(save_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    tokenizer.save(save_path)
    print("Tokenizer saved to:", save_path)


def load_tokenizer(path):
    return Tokenizer.from_file(path)


def encode_text(tokenizer, text):
    return tokenizer.encode(text)


def decode_ids(tokenizer, ids):
    return tokenizer.decode(ids)