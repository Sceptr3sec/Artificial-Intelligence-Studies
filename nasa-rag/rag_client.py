import os
import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from typing import Dict, List, Optional
from pathlib import Path

def discover_chroma_backends() -> Dict[str, Dict[str, str]]:
    """Discover available ChromaDB backends in the project directory"""
    backends = {}
    current_dir = Path(".")

    # Look for ChromaDB directories: any directory whose name contains "chroma"
    candidate_dirs = [d for d in current_dir.iterdir() if d.is_dir() and "chroma" in d.name.lower()]

    for chroma_dir in candidate_dirs:
        try:
            # Initialize database client with directory path and configuration settings
            client = chromadb.PersistentClient(
                path=str(chroma_dir),
                settings=Settings(anonymized_telemetry=False)
            )

            # Retrieve list of available collections from the database
            collections = client.list_collections()

            for collection in collections:
                collection_name = collection.name
                key = f"{chroma_dir.name}::{collection_name}"

                # Get document count with fallback for unsupported operations
                try:
                    count = collection.count()
                except Exception:
                    count = "unknown"

                backends[key] = {
                    "directory": str(chroma_dir),
                    "collection_name": collection_name,
                    "display_name": f"{chroma_dir.name} / {collection_name} ({count} docs)",
                    "document_count": count,
                }

        except Exception as e:
            # Fallback entry for inaccessible directories
            key = f"{chroma_dir.name}::error"
            error_msg = str(e)[:80]
            backends[key] = {
                "directory": str(chroma_dir),
                "collection_name": "",
                "display_name": f"{chroma_dir.name} (error: {error_msg})",
                "document_count": 0,
            }

    return backends

def initialize_rag_system(chroma_dir: str, collection_name: str, embedding_model: str = "text-embedding-3-small"):
    """Initialize the RAG system with specified backend (cached for performance)"""

    # Documents were embedded with an OpenAI model in embedding_pipeline.py. The
    # query must be embedded with the SAME model/space, or similarity search is
    # meaningless (and will error on a dimension mismatch against Chroma's
    # local default embedding function). Attaching this embedding function
    # makes collection.query(query_texts=...) embed the query with OpenAI too.
    openai_key = os.environ.get("CHROMA_OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    embedding_function = OpenAIEmbeddingFunction(
        api_key=openai_key,
        model_name=embedding_model,
    )

    client = chromadb.PersistentClient(
        path=chroma_dir,
        settings=Settings(anonymized_telemetry=False)
    )
    return client.get_collection(collection_name, embedding_function=embedding_function)

def retrieve_documents(collection, query: str, n_results: int = 3,
                      mission_filter: Optional[str] = None) -> Optional[Dict]:
    """Retrieve relevant documents from ChromaDB with optional filtering"""

    # Initialize filter variable to None (represents no filtering)
    where_filter = None

    # Check if filter parameter exists and is not set to "all" or equivalent
    if mission_filter and mission_filter.lower() != "all":
        where_filter = {"mission": mission_filter}

    # Execute database query
    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        where=where_filter,
    )

    return results

def format_context(documents: List[str], metadatas: List[Dict]) -> str:
    """Format retrieved documents into context"""
    if not documents:
        return ""

    # Chroma already returns results ordered by similarity (closest first),
    # so we preserve that order. We still dedupe exact-duplicate chunks that
    # can occur when overlapping windows retrieve the same passage twice.
    seen = set()
    deduped = []
    for doc, meta in zip(documents, metadatas):
        key = doc.strip()
        if key in seen:
            continue
        seen.add(key)
        deduped.append((doc, meta))

    if not deduped:
        return ""

    context_parts = ["Relevant NASA mission documents:"]

    for i, (doc, metadata) in enumerate(deduped, start=1):
        mission = metadata.get("mission", "unknown")
        mission = mission.replace("_", " ").title()

        source = metadata.get("source", "unknown source")

        category = metadata.get("document_category", "unknown")
        category = category.replace("_", " ").title()

        header = f"\n[Source {i}] Mission: {mission} | Category: {category} | File: {source}"
        context_parts.append(header)

        max_chars = 1500
        if len(doc) > max_chars:
            doc_content = doc[:max_chars] + "... [truncated]"
        else:
            doc_content = doc
        context_parts.append(doc_content)

    return "\n".join(context_parts)
