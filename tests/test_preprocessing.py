from preprocessing import read_conll_file

sentences, labels = read_conll_file("data/raw/train.txt")

print(sentences[:2])
print(labels[:2])
