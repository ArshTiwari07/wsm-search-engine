import re

def tokenize(text):
    return re.findall(r"\w+", text)