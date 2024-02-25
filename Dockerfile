# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

#ENV VARIABLE
ENV FLASK_DEBUG=1

# Install the application dependencies
RUN pip install -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Define the entry point for the container
CMD ["flask", "--debug", "run", "--host=0.0.0.0"]