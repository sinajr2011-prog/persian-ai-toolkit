FROM python:3.12-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml requirements.txt ./
COPY src/ ./src/
COPY app/ ./app/

# Install package
RUN pip install --no-cache-dir -e .

# Optional: install ML dependencies (comment out if you want lighter image)
# RUN pip install --no-cache-dir transformers torch

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
