import chromadb

client = chromadb.PersistentClient(path="embeddings/chroma_db")
collection = client.get_or_create_collection("rahul_memory")

results = collection.get(include=["metadatas"])
categories = [m["category"] for m in results["metadatas"] if "category" in m]
projects = [m for m in results["metadatas"] if m.get("category") == "Projects"]

print(f"Total docs: {len(results['metadatas'])}")
print(f"Projects found: {len(projects)}")

files = sorted(set([m["source"] for m in projects]))
print("\nProject files embedded:")
for f in files:
    print("-", f)
