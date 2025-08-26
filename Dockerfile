# syntax=docker/dockerfile:1
FROM python:3.11-slim


# Create non-root user and group
RUN groupadd -r appuser && useradd --no-log-init -r -g appuser appuser

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

# Set permissions for app directory
RUN chown -R appuser:appuser /app

# Expose port (default 8000)
ARG PORT=8000
ENV PORT=${PORT}
EXPOSE ${PORT}

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1


# Switch to non-root user
USER appuser

# Start FastAPI app with Uvicorn, using PORT env var
CMD ["sh", "-c", "uvicorn src.app:app --host 0.0.0.0 --port ${PORT}"]
