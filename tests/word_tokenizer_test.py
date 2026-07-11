from word_tokenizer import WordTokenizer
tokenizer = WordTokenizer()

text = "Rahul & Co. filed the petition."
tokens = tokenizer.tokenize(text)
for token in tokens:
    print(token)
