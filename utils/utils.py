import nltk.tokenize
import codecs
import logging

_tokenizer = nltk.tokenize.RegexpTokenizer(pattern=r'[\w\$]+|[^\w\s]')


def get_logger(file_name):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(file_name)

    return logger


def get_formatted_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    formatted_time = '%d:%02d:%02d' % (h, m, s)

    return formatted_time

def tokenize(text):
    """
    這邊的tokenizer 是 nltk.tokenize.RegexpTokenizer物件，會根據正規表達式將「句子」斷成一個一個word
    （在英文稱為token）
    - 輸入：一個句子
    - 輸出：一個list，裡面是tokens
    """
    tokens = _tokenizer.tokenize(text.lower())
    return tokens


class IterableSentences(object):
    def __init__(self, filename):
        self._filename = filename

    def __iter__(self):
        for line in codecs.open(self._filename, 'r', 'utf-8'):
            yield line.strip()
