# Base image
FROM python:3.1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Django port
EXPOSE 8000

# Run the Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
