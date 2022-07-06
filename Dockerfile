FROM python:3.8.5
# Run commands from /app directory inside container
WORKDIR /app
# Copy requirements from local to docker image
COPY requirements.txt .
# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir
# Copy everything from the current dir to the image
COPY . .