import json
from sentence_transformers import SentenceTransformer
import chromadb
from tqdm import tqdm

# --- Config ---
DB_PATH = "embeddings/chroma_db"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
DATA_PATH = "data/rahuls_master_dataset.json"

# --- Initialize model & Chroma DB ---
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("rahul_memory")
model = SentenceTransformer(MODEL_NAME)

# --- Flatten JSON with semantic segmentation ---
def flatten_json_to_text(obj, parent_key=''):
    texts = []

    # If it's a dictionary, go deeper
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key} {k}".strip()
            texts.extend(flatten_json_to_text(v, new_key))

    # If it's a list, process each element separately (keep atomicity)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            # Make sure each list element is treated as a separate unit
            element_texts = flatten_json_to_text(v, parent_key)
            if isinstance(v, (dict, list)):
                # join related sub-items into one paragraph for each element
                combined_text = " ".join(element_texts)
                if combined_text.strip():
                    texts.append(combined_text)
            else:
                if element_texts:
                    texts.extend(element_texts)

    # Base case: actual value
    else:
        key_clean = parent_key.replace("_", " ").replace(".", " ")
        sentence = f"{key_clean.capitalize()} is {obj}."
        texts.append(sentence)

    return texts


# --- Load data ---
print(f"📂 Loading data from: {DATA_PATH}")
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# --- Flatten JSON into segmented text blocks ---
texts = flatten_json_to_text(data)

# --- De-duplicate similar strings and clean empties ---
unique_texts = list({t.strip() for t in texts if t.strip()})
print(f"🧾 Found {len(unique_texts)} unique data entries to embed.")

# --- Generate embeddings ---
print(f"⚙️ Loading model: {MODEL_NAME}")
embeddings = model.encode(unique_texts, show_progress_bar=True, convert_to_numpy=True)

# --- Clear old entries before inserting ---
try:
    all_data = collection.get(include=["documents"])
    if all_data and all_data.get("documents"):
        collection.delete(ids=all_data["ids"])
        print("🧹 Cleared old embeddings from database.")
except Exception as e:
    print("⚠️ No previous data to clear or couldn't clear:", e)

# --- Store embeddings in Chroma ---
print("💾 Storing embeddings to database...")
collection.upsert(
    ids=[f"id_{i}" for i in range(len(unique_texts))],
    embeddings=embeddings.tolist(),
    documents=unique_texts
)

print(f"✅ Successfully embedded {len(unique_texts)} entries.")
print(f"📍 Database saved at: {DB_PATH}")
