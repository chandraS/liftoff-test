# Dockerfile for Service A
FROM python:3.8-slim

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy the application code
COPY service_a.py /app

# Expose the port the app runs on
EXPOSE 80

# Run the application
CMD ["python", "service_a.py"]
