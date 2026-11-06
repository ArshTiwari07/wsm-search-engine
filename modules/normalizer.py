import unicodedata

def normalize_text(text):
    text = unicodedata.normalize("NFKC", text)
    return text.casefold()