import os
import json
from pathlib import Path
from utils.parser import extract_relevant_sections

# Automatically detect collection folders
def get_collections(base_path="."):
    return sorted([f for f in os.listdir(base_path) if f.startswith("Collection") and os.path.isdir(f)])

# Process a single collection
def process_collection(collection_path):
    input_path = os.path.join(collection_path, "challenge1b_input.json")
    output_path = os.path.join(collection_path, "challenge1b_output.json")

    if not os.path.exists(input_path):
        print(f"[!] Skipping {collection_path}: No challenge1b_input.json found.")
        return

    print(f"📁 Processing: {collection_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = data["documents"]
    persona = data["persona"]["role"]
    task = data["job_to_be_done"]["task"]
    result = {
        "challenge_id": data["challenge_info"]["challenge_id"],
        "test_case_name": data["challenge_info"]["test_case_name"],
        "persona": persona,
        "task": task,
        "documents": []
    }

    for doc in documents:
        pdf_path = os.path.join(collection_path, "PDFs", doc["filename"])
        if not os.path.exists(pdf_path):
            print(f"  [!] Missing PDF: {pdf_path}, skipping.")
            continue

        print(f"  📄 Extracting from: {doc['filename']}")
        relevant_sections = extract_relevant_sections(pdf_path, persona, task)

        result["documents"].append({
            "filename": doc["filename"],
            "title": doc["title"],
            "relevant_sections": relevant_sections
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ Output saved: {output_path}\n")

# Main processing loop
def main():
    collections = get_collections()
    if not collections:
        print("❌ No collection folders found.")
        return

    for collection in collections:
        process_collection(collection)

if __name__ == "__main__":
    main()
