# Use the Python 3.9 slim base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt requirements.txt

# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project directory to the working directory
COPY . .

# Expose port 5000 to allow external access to the Flask application
EXPOSE 5000

# Set the command to run when the container starts
CMD ["python", "index.py"]
