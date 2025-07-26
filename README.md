# 🔍 Adobe India Hackathon – Connecting the Dots

Welcome to the solution repository for **Adobe's Connecting the Dots Hackathon 2025**.  
This repository includes implementations for:

- ✅ **Challenge 1A**: Structured Outline Extraction from PDFs
- ✅ **Challenge 1B**: Persona-Driven Document Intelligence

All solutions are designed to run **offline inside a Docker container** and adhere strictly to the challenge constraints (CPU-only, no internet, limited runtime and model size).

---

## 🧩 Repository Structure
Adobe-India-Hackathon25/
├── Challenge_1a/ # Extract outline (Title, H1/H2/H3) from PDF
│ ├── process_pdfs.py
│ ├── Dockerfile
│ ├── requirements.txt
│ ├── sample_dataset/
│ │ ├── pdfs/ # Input PDF files
│ │ ├── outputs/ # Output JSON files
│ │ └── schema/ # JSON schema for validation
│ └── README.md
│
├── Challenge_1b/ # Round 1B: Persona-Based PDF Analysis
├── Collection 1/
│ ├── PDFs/
│ ├── challenge1b_input.json
│ └── challenge1b_output.json
├── Collection 2/
│ └── ...
├── process_pdfs.py
├── utils/
│ └── parser.py
├── Dockerfile
├── README.md
│
├── README.md

## Technologies Used
Python 3.10

PyMuPDF (for PDF text extraction)

JSON I/O for structured outputs

Docker (CPU-only, offline mode)
