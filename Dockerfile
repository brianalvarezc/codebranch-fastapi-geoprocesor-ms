# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (default 8000)
ARG PORT=8000
ENV PORT=${PORT}
EXPOSE ${PORT}

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Start FastAPI app with Uvicorn, using PORT env var
CMD ["sh", "-c", "uvicorn src.app:app --host 0.0.0.0 --port ${PORT}"]
