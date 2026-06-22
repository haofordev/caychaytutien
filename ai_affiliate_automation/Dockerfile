FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (ffmpeg)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Copy requirement file and install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Create output directories
RUN mkdir -p /app/output/assets /app/output/video

# Entry point (default to help)
ENTRYPOINT ["python", "run_pipeline.py"]
