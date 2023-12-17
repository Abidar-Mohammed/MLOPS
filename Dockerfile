FROM python:3.8.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port that your FastAPI application will run on
EXPOSE 8000

# Command to run your FastAPI application
CMD ["uvicorn", "predictive-maintenance-app:app", "--host", "127.0.0.1", "--port", "8000"]
