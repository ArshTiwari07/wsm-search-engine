import fnmatch

def expand_wildcard(pattern, vocabulary):
    pattern = pattern.casefold()

    return [
        word for word in vocabulary
        if fnmatch.fnmatchcase(word, pattern)
    ]