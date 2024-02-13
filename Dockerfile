# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV NAME World

# Run main_app.py when the container launches
# CMD ["python", "main_app.py"]
CMD python ./app.py