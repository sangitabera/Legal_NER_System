from parser import LegalDatasetParser
parser = LegalDatasetParser()
documents = parser.parse_directory("data/train")
print(len(documents))
print(documents[0])
print(documents[0].entities)