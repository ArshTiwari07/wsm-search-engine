from modules.normalizer import normalize_text
from modules.tokenizer import tokenize
from modules.wildcard_processor import expand_wildcard

def search_query(query, index):

    terms = query.split()

    if not terms:
        return []

    result = None

    for term in terms:

        term = normalize_text(term)

        if "*" in term or "?" in term:
            matches = expand_wildcard(term, index.keys())
        else:
            matches = [term] if term in index else []

        term_result = set()

        for word in matches:
            term_result.update(index.get(word, set()))

        if result is None:
            result = term_result
        else:
            result.intersection_update(term_result)

    return sorted(result) if result else []