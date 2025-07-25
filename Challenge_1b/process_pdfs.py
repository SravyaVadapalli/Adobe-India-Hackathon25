import json
import os
from utils.parser import extract_text_from_pdf

def load_input_config(path):
    """Load the input configuration JSON."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def process_documents(input_config, collection_path):
    """Extract and analyze documents for a given collection."""
    pdf_dir = os.path.join(collection_path, "PDFs")
    output_path = os.path.join(collection_path, "challenge1b_output.json")

    output = {
        "metadata": {
            "input_documents": [],
            "persona": input_config["persona"]["role"],
            "job_to_be_done": input_config["job_to_be_done"]["task"]
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for doc in input_config["documents"]:
        filename = doc["filename"]
        title = doc["title"]
        filepath = os.path.join(pdf_dir, filename)

        if not os.path.exists(filepath):
            print(f"❌ File not found: {filepath}")
            continue

        text_pages = extract_text_from_pdf(filepath)
        output["metadata"]["input_documents"].append(filename)

        # Process first 3 pages as a sample
        for i, page_data in enumerate(text_pages[:3]):
            output["extracted_sections"].append({
                "document": filename,
                "section_title": title,
                "importance_rank": i + 1,
                "page_number": page_data["page_number"]
            })
            output["subsection_analysis"].append({
                "document": filename,
                "refined_text": page_data["text"][:300],
                "page_number": page_data["page_number"]
            })

    # Write output JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"✅ Output written to {output_path}")

def main():
    """Main driver for processing all collections."""
    collections = ["Collection 1", "Collection 2", "Collection 3"]

    for collection in collections:
        input_path = os.path.join(collection, "challenge1b_input.json")

        if os.path.exists(input_path):
            print(f"\n📁 Processing {collection}")
            input_config = load_input_config(input_path)
            process_documents(input_config, collection)
        else:
            print(f"⚠️ Skipping {collection}: No input JSON found.")

if __name__ == "__main__":
    main()