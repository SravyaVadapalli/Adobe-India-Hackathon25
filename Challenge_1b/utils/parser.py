import fitz  # PyMuPDF
import re

def extract_relevant_sections(pdf_path, persona, task):
    relevant_sections = []

    try:
        doc = fitz.open(pdf_path)
        full_text = ""

        for page in doc:
            text = page.get_text()
            if text:
                full_text += text + "\n"

        # Split into paragraphs for cleaner relevance checks
        paragraphs = [p.strip() for p in full_text.split("\n\n") if len(p.strip()) > 50]

        # Simple rule-based relevance: look for task-related or persona-related keywords
        keywords = generate_keywords(persona, task)

        for para in paragraphs:
            if any(re.search(rf"\b{kw}\b", para, re.IGNORECASE) for kw in keywords):
                relevant_sections.append(para)

        # Limit to top 5 most relevant sections
        return relevant_sections[:5] if relevant_sections else paragraphs[:2]

    except Exception as e:
        print(f"[!] Error processing {pdf_path}: {e}")
        return []

def generate_keywords(persona, task):
    # Extract keywords from persona and task
    combined = f"{persona} {task}".lower()
    tokens = re.findall(r'\b[a-zA-Z]{4,}\b', combined)
    return list(set(tokens))  # Remove duplicates
