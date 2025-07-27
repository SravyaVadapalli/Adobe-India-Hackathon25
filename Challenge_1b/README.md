# Challenge 1b: Multi-Collection PDF Analysis

## Overview
Advanced PDF analysis solution that processes multiple document collections and extracts relevant content based on specific personas and use cases.

## Project Structure
```
Challenge_1b/
├── Collection 1/ # Travel Planning
│ ├── PDFs/ # Input documents
│ ├── challenge1b_input.json # Input persona & task description
│ └── challenge1b_output.json # Output with extracted structured content
├── Collection 2/ # Adobe Acrobat Learning
├── Collection 3/ # Recipe Collection
├── Dockerfile # Docker setup for reproducible environment
├── process_pdfs.py # Main runner for processing
├── requirements.txt # Python dependencies
└── utils/
└── parser.py # PDF parsing and text extraction logic
```

## ⚙️ How It Works

### Input
- Each `Collection` has:
  - `PDFs/` folder containing relevant documents
  - `challenge1b_input.json` describing the **persona**, **task**, and **document list**

### Processing
- PDFs are parsed using `pdfminer.six`
- Relevant content is extracted based on the persona and task
- Sections are ranked based on relevance using keyword matching, embeddings, or other logic

### Output
- `challenge1b_output.json` with:
  - Metadata (persona, task, timestamp)
  - Extracted sections with page number, importance ranking
  - Refined subsection text

---

## 🚀 Running the Project via Docker

### 1️⃣ Build the Docker Image

```bash
docker build -t adobe-challenge-1b .
```

### 2️⃣ Run the Container
```docker run --rm `
  -v "${PWD}/Collection 1/PDFs:/app/input" `
  -v "${PWD}/Collection 1:/app/output" `
  adobe-challenge-1b
```

### Input JSON Structure
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_001",
    "test_case_name": "menu_planning",
    "description": "Dinner menu planning"
  },
  "documents": [
    { "filename": "Dinner Ideas - Sides_1.pdf", "title": "Dinner Ideas - Sides_1" },
    ...
  ],
  "persona": {
    "role": "Food Contractor"
  },
  "job_to_be_done": {
    "task": "Prepare a vegetarian buffet-style dinner menu for a corporate gathering, including gluten-free items."
  }
}
```

### Output JSON Structure
```json
{
  "metadata": {
    "input_documents": [...],
    "persona": "Food Contractor",
    "job_to_be_done": "...",
    "processing_timestamp": "2025-07-24T13:00:00"
  },
  "extracted_sections": [
    {
      "document": "...",
      "section_title": "...",
      "importance_rank": 1,
      "page_number": 3
    },
    ...
  ],
  "subsection_analysis": [
    {
      "document": "...",
      "refined_text": "...",
      "page_number": 3
    },
    ...
  ]
}
```

## Key Features
- Persona-based content analysis
- Importance ranking of extracted sections
- Multi-collection document processing
- Structured JSON output with metadata
