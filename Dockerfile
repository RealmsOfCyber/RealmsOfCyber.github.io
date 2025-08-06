# Dockerfile for the ROC website
#
# Build the image:
# docker build -t realmsofcyber-site .
#
# Run the container:
# docker run -p 8000:8000 realmsofcyber-site
#
# Access the website at http://localhost:8000

# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Generate the static site
RUN python3 generate.py

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run a simple web server
CMD ["python3", "-m", "http.server", "--directory", "site", "8000"]
