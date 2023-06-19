# Start from a base image. We're using the official Python image from Docker Hub,
# which has Python 3.11 installed.
FROM python:3.11

# Set the working directory in the Docker image to /app. All following instructions 
# in the Dockerfile will be run in this directory.
WORKDIR /app

# Copy the contents of the current directory on your computer (i.e., your project files) 
# into the /app directory in the Docker image.
COPY . /app

# Install the Python dependencies from requirements.txt.
# --no-cache-dir option is used to keep the image small.
RUN pip install --no-cache-dir -r requirements.txt

# At runtime, this will run profiler.py with python
CMD ["python", "profiler.py"]
