# Use Ubuntu as the base image
FROM ubuntu:latest

RUN mkdir /app
COPY main.cc /app
COPY test.sh /app


# Update the package lists
RUN apt-get update

# Install g++ compiler
RUN apt-get install -y g++
