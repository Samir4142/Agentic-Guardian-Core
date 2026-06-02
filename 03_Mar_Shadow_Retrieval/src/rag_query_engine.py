import ollama
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from colorama import Fore, init
import os

init(autoreset=True)

# --- CONFIGURATION ---
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
knowledge_path = os.path.join(ROOT_DIR, "data", "company_knowledge")
model_name = "llama3"


def run_rag_system():
    print(Fore.YELLOW + "--- INITIATING RAG QUERY ENGINE ---\n")

    # 1. Re-Initialize The Knowledge Base (Since It Is In-Memory)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    loader = DirectoryLoader(
        knowledge_path, glob="./*.txt", loader_cls=TextLoader)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(docs)
    vector_db = DocArrayInMemorySearch.from_documents(chunks, embeddings)

    # 2. The User Query
    user_query = "What Are The Rules For The Server Room?"
    print(Fore.CYAN + f"[User] Query: {user_query}")

    # 3. Retrieval: Find Relevant Chunks
    relevant_docs = vector_db.similarity_search(user_query, k=2)
    context_text = "\n".join([d.page_content for d in relevant_docs])

    # 4. Augmentation: Combine Context With System Prompt
    system_prompt = f"""
    You Are A Helpful Corporate Assistant.
    Answer The Question ONLY Using The Provided Context.
    If The Answer Is Not In The Context, Say You Do Not Know.
    
    CONTEXT:
    {context_text}
    """

    # 5. Generation: Get Final Answer From Llama-3
    print(Fore.CYAN + "[Agent] Thinking...")
    response = ollama.chat(model=model_name, messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_query}
    ])

    print(Fore.GREEN + f"\n[Final Answer]\n{response['message']['content']}")


if __name__ == "__main__":
    run_rag_system()
