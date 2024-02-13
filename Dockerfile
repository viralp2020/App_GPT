# Use an official Python runtime as a parent image
FROM ubuntu:latest
RUN apt update
run apt install python3-pip -y

# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV NAME World

# Run main_app.py when the container launches
#CMD ["python3", "main_app.py"]
CMD python3 ./app.py