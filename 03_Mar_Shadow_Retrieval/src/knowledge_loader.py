import ollama
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import DocArrayInMemorySearch  # Alternative Store
from langchain_ollama import OllamaEmbeddings
from colorama import Fore, init
import os

# Initialize Terminal Colors
init(autoreset=True)

# --- CONFIGURATION VARIABLES ---
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
knowledge_path = os.path.join(ROOT_DIR, "data", "company_knowledge")
embedding_model = "nomic-embed-text"


def initialize_vector_store():
    print(Fore.YELLOW + "--- INITIATING VECTOR ARCHITECTURE SETUP (V3 - COMPATIBILITY MODE) ---\n")

    try:
        # 1. Load Documents
        print(Fore.CYAN + f"[+] Loading Documents From: {knowledge_path}")
        loader = DirectoryLoader(
            knowledge_path, glob="./*.txt", loader_cls=TextLoader)
        docs = loader.load()

        # 2. Split Text Into Chunks
        print(Fore.CYAN + "[+] Splitting Text Into Mathematical Chunks...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(docs)

        # 3. Initialize The Embedding Engine
        print(Fore.CYAN +
              f"[+] Initializing Embedding Engine: {embedding_model}...")
        embeddings = OllamaEmbeddings(model=embedding_model)

        # 4. Create In-Memory Vector Database
        print(Fore.CYAN + "[+] Generating In-Memory Vector Store...")
        vector_db = DocArrayInMemorySearch.from_documents(
            documents=chunks,
            embedding=embeddings
        )

        print(Fore.GREEN +
              "\n[!] SUCCESS: Knowledge Base Initialized In Memory.")

        # 5. Quick Test: Perform A Similarity Search
        query = "What Is The Wifi Password?"
        search_results = vector_db.similarity_search(query)
        print(Fore.WHITE + f"\n[Test Search] Query: '{query}'")
        print(Fore.WHITE +
              f"[Test Result] Top Match: {search_results[0].page_content}")

        return vector_db

    except Exception as e:
        print(
            Fore.RED + f"[!] ERROR: Failed To Initialize Knowledge Base. \n{e}")
        return None


if __name__ == "__main__":
    initialize_vector_store()
