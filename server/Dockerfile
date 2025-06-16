FROM python:3.13.5-slim-bookworm

# Prevents interactive prompts during package install
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Copy project files first (better for cache usage)
COPY . .

# Install system dependencies and Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends nasm binutils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
