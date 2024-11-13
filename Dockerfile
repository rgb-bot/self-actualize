# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /sendMessage

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/sendMessage

# Copy the contents of the current directory (host machine) into the container's /app directory
COPY . /sendMessage

# Expose port and start the application
EXPOSE 8020
CMD ["python", "app/api.py"]