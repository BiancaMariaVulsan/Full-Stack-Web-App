# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=backend.settings

# Run the Django development server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
