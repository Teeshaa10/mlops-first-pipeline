#Start with a base image containing Python runtime
#This  gives our container a Python environment to run our code
FROM python:3.14-slim
#Set the working directory in the container
WORKDIR /app
#Copy the dependencies list before copying application code
COPY requirements.txt .
#avoid retaining pip's download cache in the image layer to reduce image size 
RUN pip install --no-cache-dir -r requirements.txt
#Copy the content of the local src directory to the working directory
COPY . .
#Document the port used by FASTAPI app
EXPOSE 8000
#Start the API server using uvicorn when the container launches
#0.0.0.0 allows connections through the container's network interface, and 8000 is the port number
CMD ["uvicorn", "main:app", "--host", "0.0.0", "--port", "8000"]

