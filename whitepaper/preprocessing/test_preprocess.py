import gensim
import mock
import pytest

from preprocessing.preprocess import Preprocess


@mock.patch('tika.parser.from_file')
@mock.patch('preprocessing.preprocess.Preprocess.__init__')
def test_read(mock_Preprocess_init, mock_parser):
    mock_Preprocess_init.return_value = None
    mock_parser.return_value = {'content': 'test content', 'metadata': {'xmpTPg:NPages': '1'}}
    processor = Preprocess()
    assert(processor.read(None) == ('1', 'test content'))

@mock.patch('preprocessing.preprocess.Preprocess.__init__')
def test_tokenize(mock_Preprocess_init):
    mock_Preprocess_init.return_value = None
    text = 'Hello World! I love you 2.'
    processor = Preprocess()
    assert(processor.tokenize(text) == ['hello', 'world', 'i', 'love', 'you', '2'])

@mock.patch('preprocessing.preprocess.Preprocess.__init__')
def test_split_in_sentences(mock_Preprocess_init):
    mock_Preprocess_init.return_value = None
    text = 'Hello World! I love you 2.'
    processor = Preprocess()
    assert(processor.split_in_sentences(text) == ['Hello World!', 'I love you 2.'])


@mock.patch('preprocessing.preprocess.Preprocess.__init__')
def test_create_tagged_documents(mock_Preprocess_init):
    mock_Preprocess_init.return_value = None
    documents = {'ABC': ['hello', 'world', 'i', 'love', 'you', '2']}
    processor = Preprocess()
    assert(processor.create_tagged_documents(documents) == [gensim.models.doc2vec.TaggedDocument(['hello', 'world', 'i', 'love', 'you', '2'], ['ABC'])])
