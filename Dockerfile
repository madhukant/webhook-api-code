# Use the official Python image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask

# Expose port 5000 to the outside world
EXPOSE 5000

# Run main.py when the container launches
CMD ["python", "main.py"]
