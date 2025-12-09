# Use Python 3.13 base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -e ".[dev]"

# Set PYTHONPATH to include src directory
ENV PYTHONPATH=/app/src

# Expose port for web application
EXPOSE 5000

# Run the web application when container starts
CMD ["python", "-m", "todo_app.web"]