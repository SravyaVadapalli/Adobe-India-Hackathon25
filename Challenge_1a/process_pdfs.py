import os
import json
from pathlib import Path
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def get_heading_level(font_size):
    if font_size >= 16:
        return "H1"
    elif 13 <= font_size < 16:
        return "H2"
    elif 10 <= font_size < 13:
        return "H3"
    return None

def extract_outline(pdf_path):
    outline = []
    doc_title = ""
    max_font_size = 0

    for page_number, layout in enumerate(extract_pages(pdf_path), start=1):
        for element in layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    if not hasattr(text_line, "__iter__"):
                        continue
                    font_sizes = [char.size for char in text_line if isinstance(char, LTChar)]
                    if font_sizes:
                        avg_size = sum(font_sizes) / len(font_sizes)
                        text = text_line.get_text().strip()

                        if not text:
                            continue

                        # Get document title from first page
                        if page_number == 1 and avg_size > max_font_size:
                            max_font_size = avg_size
                            doc_title = text

                        level = get_heading_level(avg_size)
                        if level:
                            outline.append({
                                "level": level,
                                "text": text,
                                "page": page_number
                            })

    return {
        "title": doc_title,
        "outline": outline
    }

def main():
    print(f"📥 Checking input directory: {INPUT_DIR}")
    input_path = Path(INPUT_DIR)
    output_path = Path(OUTPUT_DIR)

    if not input_path.exists():
        print("❌ ERROR: Input directory not found.")
        return

    output_path.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_path.glob("*.pdf"))
    print(f"📄 PDF files found: {[f.name for f in pdf_files]}")

    for pdf_file in pdf_files:
        print(f"🔍 Processing: {pdf_file.name}")
        try:
            output_json = extract_outline(pdf_file)
            output_file = output_path / (pdf_file.stem + ".json")
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(output_json, f, indent=2)
            print(f"✅ Saved: {output_file}")
        except Exception as e:
            print(f"❌ Error processing {pdf_file.name}: {e}")

if __name__ == "__main__":
    main()