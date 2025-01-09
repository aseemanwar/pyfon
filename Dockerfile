# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY app.py /app/

# Install any necessary Python dependencies
RUN pip install --no-cache-dir ddtrace

# Set environment variables for Datadog
ENV DD_SERVICE="example-service" \
    DD_ENV="production" \
    DD_VERSION="1.0.0"

# Run the application
CMD ["python", "app.py"]
