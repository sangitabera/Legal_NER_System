from dataset.tokenizer import train_tokenizer
train_tokenizer(
    files = ["data/raw/train.txt"],
    save_path = "data/tokenizer/legal_bpe.json",
    vocab_size= 10
)