## Indexly — WSM Document Search Engine

A modular, Python-based document search application built for a Web Search and Mining (WSM) assignment. Indexly loads a collection of text files, normalizes and tokenizes their contents, builds an inverted index, and lets users search the collection through a Tkinter desktop GUI.

## Features

- **Document loading:** Reads `.txt` files from the document collection.
- **Tokenization:** Splits text into searchable terms.
- **Text normalization:** Applies Unicode normalization and case folding for case-insensitive matching.
- **Inverted index:** Maps each term to the documents in which it appears.
- **Query processing:** Supports multi-term AND searches.
- **Wildcard search:** Supports `*` (zero or more characters) and `?` (exactly one character).
- **Desktop GUI:** Provides a search input, Search button, and read-only results area.

## Project structure

```text
WSM_Search_Engine/
│
├── main.py
│
├── modules/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── tokenizer.py
│   ├── normalizer.py
│   ├── indexer.py
│   ├── query_processor.py
│   └── wildcard_processor.py
│
├── frontend/
│   ├── __init__.py
│   └── gui.py
│
├── data/
│   └── documents/
│       ├── doc1.txt
│       ├── doc2.txt
│       └── doc3.txt
│
└── README.md
```

## Requirements

- Python 3.8 or later
- Tkinter (usually included with standard Python installations)

The project uses Python's standard library and does not require third-party packages.

> **Note:** On some Linux distributions, Tkinter may need to be installed separately (for example, through the system package `python3-tk`).

## Setup and execution

1. Clone or download this project.
2. Open the project folder in a terminal or VS Code.
3. Place your `.txt` files inside `data/documents/`.
4. Make sure the folder and module names match the project structure above.
5. Run the application from the project root:

```bash
python main.py
```

If your system uses `python3` as the Python command, run:

```bash
python3 main.py
```

The GUI should open in a desktop window. Enter a query and click **Search**, or press Enter.

## How it works

### 1. Document loading

`document_loader.py` reads every `.txt` file in `data/documents/` and stores its filename and content.

### 2. Tokenization

`tokenizer.py` splits text into individual word tokens.

### 3. Text normalization / case folding

`normalizer.py` applies Unicode NFKC normalization and `casefold()`. This makes matching case-insensitive and helps standardize equivalent Unicode text.

### 4. Inverted index construction

`indexer.py` processes each document and builds an inverted index. Each term points to the set of document filenames containing that term.

Example:

```python
{
    "python": {"doc1.txt", "doc3.txt"},
    "java": {"doc2.txt"},
    "learning": {"doc1.txt", "doc3.txt"}
}
```

### 5. Query processing

`query_processor.py` normalizes and tokenizes the query, retrieves the documents associated with each term, and intersects those sets. Therefore, a multi-word query uses **AND semantics**: a document is returned only if it contains every query term.

### 6. Wildcard processing

`wildcard_processor.py` expands wildcard terms against the vocabulary in the inverted index using filename-style pattern matching:

- `*` matches zero or more characters.
- `?` matches exactly one character.

Examples:

| Query | Meaning |
|---|---|
| `py*` | Terms beginning with `py` |
| `pro*` | Terms beginning with `pro` |
| `j?va` | Four-character terms beginning with `j` and ending with `va` |
| `*ing` | Terms ending with `ing` |

### 7. Frontend GUI

`frontend/gui.py` provides the desktop interface. It accepts a search query, calls the search function supplied by `main.py`, and displays matching document filenames in a read-only result area.

## Example searches

Assuming the sample documents contain the example text supplied with the project:

| Search query | Expected result |
|---|---|
| `python` | Documents containing `python` |
| `java` | Documents containing `java` |
| `machine learning` | Documents containing both terms |
| `pro*` | Documents containing a term beginning with `pro` |
| `j?va` | Documents containing the term `java` |

The exact results depend on the text files present in `data/documents/`.

## Adding documents

To index additional documents:

1. Create or copy a `.txt` file into `data/documents/`.
2. Restart the application by running `python main.py` again.

The index is built when the application starts, so files added while it is running are not included until the next launch.

## Current limitations

- Only `.txt` files are loaded.
- Search uses AND semantics for multiple terms.
- Results are document filenames; relevance ranking is not implemented.
- Phrase searching and positional indexing are not implemented.
- Wildcards are expanded by scanning the indexed vocabulary.
- The index is rebuilt in memory each time the application starts.

## Troubleshooting

**The GUI does not open**

- Confirm that Python is installed.
- Check that Tkinter is available: `python -m tkinter`.
- On Linux, install the distribution's Tkinter package if necessary.

**No documents are found**

- Confirm that `.txt` files are inside `data/documents/`.
- Run `main.py` from the project root so the relative data path resolves correctly.
- Restart the application after adding or editing documents.

**A module import error occurs**

- Check that all module filenames and folder names match the project structure.
- Ensure `__init__.py` exists in both `modules/` and `frontend/`.
- Run the command from the root `WSM_Search_Engine/` directory.

## Academic scope

This project demonstrates the basic stages of an information retrieval system: document collection, tokenization, normalization, inverted-index construction, query evaluation, wildcard matching, and a graphical search interface.

---

**Project:** WSM Document Search Engine  
**Language:** Python  
**GUI toolkit:** Tkinter  
**Index structure:** Inverted index
"""

output_path = "/mnt/data/README.md"
pypandoc.convert_text(readme, "md", format="md", outputfile=output_path, extra_args=["--standalone"])
print(output_path)
