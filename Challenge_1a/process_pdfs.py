from pathlib import Path
import fitz 
import json

def extract_text_from_pdf(pdf_path):
    """Extract text content from each page of the PDF."""
    doc = fitz.open(pdf_path)
    pages = []

    for page in doc:
        page_data = {
            "page_number": page.number + 1,
            "text": page.get_text()
        }
        pages.append(page_data)

    extracted_data = {
        "filename": pdf_path.name,
        "total_pages": doc.page_count,
        "pages": pages
    }
    doc.close()
    return extracted_data

def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")

    print("Checking input directory:", input_dir)
    print("Directory exists:", input_dir.exists())
    print("PDF files found:", list(input_dir.glob("*.pdf")))

    if not input_dir.exists():
        print("❌ ERROR: Input directory not found.")
        return

    for pdf_file in input_dir.glob("*.pdf"):
        print(f"Processing: {pdf_file.name}")
        doc = fitz.open(pdf_file)
        pages = []
        for page in doc:
            pages.append({"page_number": page.number + 1, "text": page.get_text()})
        output_path = output_dir / f"{pdf_file.stem}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({"filename": pdf_file.name, "total_pages": len(pages), "pages": pages}, f, indent=2)
        print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    process_pdfs()