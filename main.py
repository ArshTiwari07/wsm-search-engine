from modules.document_loader import load_documents
from modules.indexer import build_index
from modules.query_processor import search_query
from frontend.gui import SearchGUI

# Load documents
documents = load_documents("data/documents")

# Build inverted index
index = build_index(documents)

# Connect query processing
def perform_search(query):
    return search_query(query, index)

# Start GUI
app = SearchGUI(perform_search)
app.run()