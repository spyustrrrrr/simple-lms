# Base image - Python 3.11 slim untuk ukuran image yang lebih kecil
FROM python:3.11-slim

# Set environment variables
# Mencegah Python membuat file .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Mencegah Python buffering stdout dan stderr
ENV PYTHONUNBUFFERED=1

# Set working directory di dalam container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements terlebih dahulu (untuk Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy seluruh project ke dalam container
COPY . .

# Buat direktori untuk static files
RUN mkdir -p /app/staticfiles

# Expose port 8000
EXPOSE 8000

# Script entrypoint untuk menjalankan server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
