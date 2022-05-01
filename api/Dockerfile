FROM ubuntu:latest
RUN apt update  
RUN apt install -y python3
WORKDIR /api
RUN apt update 
RUN apt-get install -y build-essential
RUN apt-get install -y python3-pip
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["/bin/sh", "/api/runner.sh"]

