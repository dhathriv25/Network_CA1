# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies (using requirements.txt for better scalability)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

