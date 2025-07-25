FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy code
COPY process_pdfs.py .

# Install dependencies
RUN pip install pdfminer.six

# Create input/output folders
RUN mkdir -p /app/input /app/output

# Default command
CMD ["python", "process_pdfs.py"]