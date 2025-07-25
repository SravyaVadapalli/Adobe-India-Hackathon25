# 🧠 Challenge 1a: PDF Outline Extraction

## 📘 Overview

This tool extracts a **structured outline** from a raw PDF file, providing:

* 📌 **Document Title**
* 🔠 **Headings**: H1, H2, H3
* 📄 **Page Number** where each heading appears

---

## 📅 Input

A single PDF file (max 50 pages) placed in:

```
/app/input/
```

---

## 📄 Output

A JSON file with the following format saved to:

```
/app/output/
```

### 🔧 Sample Output

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

---

## 🧹 Approach

### 📄 PDF Parsing

* Utilizes `pdfminer.six` to extract layout data
* Parses each page to analyze text blocks (`LTTextContainer`) and character-level font sizes (`LTChar`)

### 🍿 Title Extraction

* The line with the **largest font size on the first page** is selected as the **document title**

### 🔢 Heading Detection

* Average font size is calculated for each line
* Based on the average, headings are classified as:

  * **H1**: ≥ 16 pt
  * **H2**: 13–15.9 pt
  * **H3**: 10–12.9 pt

> ⚙️ These thresholds are configurable

### 🧾 JSON Construction

* Outputs title and structured headings with level and page number into a JSON file

---

## 📁 Project Structure

```
Challenge_1a/
├── sample_dataset/
│   ├── pdfs/            # Input PDF files
│   ├── outputs/         # Output JSON files
│   └── schema/
│       └── output_schema.json
├── process_pdfs.py      # Core processing script
├── Dockerfile           # Docker setup
└── README.md            # Project documentation
```

---

## ✅ Requirements

* ❌ No internet access
* ❌ No GPU required
* ⏱️ Executes within 10 seconds (for ≤ 50-page PDF)
* 🟣 Docker-compatible (Linux/AMD64)
* 📆 Model size ≤ 200MB *(no ML model used here)*

---

## 🐳 Docker Setup

### 📄 Dockerfile

```Dockerfile
FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app
COPY process_pdfs.py .
RUN pip install --no-cache-dir pdfminer.six

CMD ["python", "process_pdfs.py"]
```

---

## 🔨 Build Docker Image

```bash
docker build --platform linux/amd64 -t pdf-processor .
```

---

## 🚀 Run Docker Container

```bash
docker run --rm ^
  -v "D:\Sravya\docker\Challenge_1a\sample_dataset\pdfs:/app/input:ro" ^
  -v "D:\Sravya\docker\Challenge_1a\sample_dataset\outputs:/app/output" ^
  --network none ^
  pdf-processor
```

---

## 📌 Notes

* All paths should be **adjusted** to match your host system
* Make sure the `/app/input` and `/app/output` directories are properly mounted

---

Feel free to reach out for test cases or output visualization examples!