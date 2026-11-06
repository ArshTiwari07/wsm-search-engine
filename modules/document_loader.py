from pathlib import Path

def load_documents(folder):
    documents = {}

    for file in Path(folder).glob("*.txt"):
        documents[file.name] = file.read_text(
            encoding="utf-8"
        )

    return documents