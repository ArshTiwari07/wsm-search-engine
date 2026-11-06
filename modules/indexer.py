from collections import defaultdict
from modules.normalizer import normalize_text
from modules.tokenizer import tokenize

def build_index(documents):
    inverted_index = defaultdict(set)

    for doc_id, content in documents.items():

        normalized = normalize_text(content)
        tokens = tokenize(normalized)

        for word in tokens:
            inverted_index[word].add(doc_id)

    return dict(inverted_index)