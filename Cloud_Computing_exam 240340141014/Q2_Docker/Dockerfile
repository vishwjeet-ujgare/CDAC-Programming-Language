# Use an official Ubuntu runtime as the base image
FROM ubuntu:latest

# Update the system and install Python3 and pip
RUN apt-get update -y && apt-get install -y python3 python3-pip

# Seting  working directory in the container
WORKDIR /app


# Copy the current directory contents into the container at /app
COPY . /app

CMD ["python","app.py"]

# create docker file with the appropirate instructions for installing Ubuntu OS and anyy dependencies required for running for python appliacaton

# write a simple python script eg.app.py print "Hello world" when excuted

# buila docker image using dockerfile created in step a ensure the pythonscript is cpied into image

# deploe a container using the docker image buld in step c

# veryfy that conainer is running by checking ita statusc and accessing th pyson aplllicaoni 


