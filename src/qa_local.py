import json, os, re, difflib, subprocess
from sentence_transformers import SentenceTransformer
import chromadb

DB_PATH = "embeddings/chroma_db"
DATA_DIR = "data"
MODEL_NAME = "phi3"
OLLAMA_PATH = r"C:/Users/Lenovo/AppData/Local/Programs/Ollama/ollama.exe"

# --- Load probable QnA once ---
with open(os.path.join(DATA_DIR, "probable_qna.json"), "r", encoding="utf-8") as f:
    probable_qna = json.load(f)

# --- Load other JSON parts ---
def load_json(name):
    with open(os.path.join(DATA_DIR, f"{name}.json"), "r", encoding="utf-8") as f:
        return json.load(f)

profile = load_json("profile")
education = load_json("education")
skills = load_json("skills")
projects = load_json("projects")
achievements = load_json("achievements")

# --- Match user question against probable QnA ---
def check_probable_qna(question, threshold=0.75):
    best_match = None
    highest_ratio = 0

    for qa in probable_qna:
        ratio = difflib.SequenceMatcher(None, question.lower(), qa["question"].lower()).ratio()
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = qa

    if highest_ratio >= threshold:
        return best_match["answer"]
    return None

# --- Select relevant section based on keywords ---
def choose_context(question):
    q = question.lower()
    if any(k in q for k in ["project", "app", "website","projects"]):
        return json.dumps(projects, ensure_ascii=False)
    elif any(k in q for k in ["degree", "college", "education", "course"]):
        return json.dumps(education, ensure_ascii=False)
    elif any(k in q for k in ["skill", "tech", "language"]):
        return json.dumps(skills, ensure_ascii=False)
    elif any(k in q for k in ["award", "rank", "certificate", "achievement"]):
        return json.dumps(achievements, ensure_ascii=False)
    else:
        return json.dumps(profile, ensure_ascii=False)

# --- Ask model ---
def ask_model(question, context  , timeout=120):
    prompt = f" You are Rahul Kumar Parida's personal AI assistant.You have access to Rahul's verified knowledge, background, education, projects, and achievements from the dataset below.Rules:1. Answer ONLY using the provided context.2. NEVER invent or assume anything not stated here.3. If the answer cannot be found, reply exactly with: The available data does not contain this information.4. Do not refer to JSON keys or technical fields — speak naturally, as if describing a person.Answer this question strictly based on the JSON data below:\n\n{context}\n\nQuestion: {question}\nAnswer:"
    try:
        process = subprocess.Popen(
            [OLLAMA_PATH, "run", MODEL_NAME],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=False
        )
        stdout, stderr = process.communicate(input=prompt.encode("utf-8") )
        return stdout.decode("utf-8", errors="ignore").strip()
    except subprocess.TimeoutExpired:
        process.kill()
        return "⚠️ Model timed out."
    except Exception as e:
        return f"⚠️ Error: {e}"

# --- Main interaction loop ---
print("💬 Rahul-AI Hybrid (QnA + Context Routing)")
while True:
    q = input("\nAsk Rahul-AI: ").strip()
    if not q:
        break

    # 1️⃣ Try probable QnA first
    answer = check_probable_qna(q)
    if answer:
        print("\n🧠", answer)
        continue

    # 2️⃣ Route to correct context
    context = choose_context(q)
    print("🔍 Context:", "projects" if "project" in q else "profile", "\n")
    response = ask_model(q, context)
    print("\n🧠", response)
