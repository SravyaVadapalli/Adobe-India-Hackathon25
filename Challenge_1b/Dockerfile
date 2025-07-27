# Use a slim Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency list first and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files into container
COPY . .

# Set default command to run the processing script
CMD ["python", "process_pdfs.py"]
