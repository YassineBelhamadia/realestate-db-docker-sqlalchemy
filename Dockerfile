# Use the official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /projetBrief3

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variable to prevent Python buffering
ENV PYTHONUNBUFFERED=1

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Define the default command
CMD ["python", "app.py"]
