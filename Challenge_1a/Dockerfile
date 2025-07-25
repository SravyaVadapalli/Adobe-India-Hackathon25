# Use official Python slim image for smaller size
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the processing script into the container
COPY process_pdfs.py .

# Install required Python packages (PyMuPDF)
RUN pip install --no-cache-dir pymupdf

# Set the default command to run the script
CMD ["python", "process_pdfs.py"]