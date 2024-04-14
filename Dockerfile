# Use the official Python image as a base
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]