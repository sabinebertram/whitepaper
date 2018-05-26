import gensim
import nltk
import tika
from tika import parser


class Preprocess():

    def __init__(self):
        tika.initVM()
        nltk.download('punkt')

    def read(self, filepath):
        pdf = parser.from_file(filepath)
        pages = pdf.get('metadata').get('xmpTPg:NPages')
        raw_text = pdf.get('content')
        ascii_text = raw_text.encode('ascii',errors='ignore').decode()
        return (pages, ascii_text)

    def tokenize(self, text):
        tokens = nltk.tokenize.word_tokenize(text)
        alphanumerical_tokens = [token.lower() for token in tokens if token.isalnum()]
        return alphanumerical_tokens

    def split_in_sentences(self, text):
        sentences = nltk.tokenize.sent_tokenize(text)
        return sentences

    def create_tagged_documents(self, documents):
        tagged_documents = []
        for name, tokens in documents.items():
            tagged_document = gensim.models.doc2vec.TaggedDocument(tokens, [name])
            tagged_documents.append(tagged_document)
        return tagged_documents
