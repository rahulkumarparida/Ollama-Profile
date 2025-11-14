import chromadb

client = chromadb.PersistentClient(path="embeddings/chroma_db")
collection = client.get_or_create_collection("rahul_memory")

query = "What are Rahul's projects?"
results = collection.query(query_texts=[query], n_results=10)
context = "\n".join(results["documents"][0])

results = collection.query( 
    query_texts=[query],
    n_results=5,
    where={"category": "Projects"}  # filter only project-related chunks
)

for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
    print("\n---")
    print("Source:", meta["source"])
    print("Category:", meta["category"])
    print(doc[:300], "...")
