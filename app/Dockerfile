# --- Base Stage ---
# Use an official lightweight Python image
FROM python:3.9-slim

# --- Build Stage ---
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
# (In this simple case, we install Flask directly)
# For a real app, you would copy a requirements.txt file first:
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Flask
RUN pip install Flask==2.1.2

# Copy the rest of the application source code into the container
COPY . .

# --- Final Stage ---
# Expose the port the app runs on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]
