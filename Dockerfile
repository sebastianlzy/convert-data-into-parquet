#Deriving the latest base image
FROM python:latest


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /

#to COPY the remote file at working directory in container
COPY ./hello_world/requirements.txt ./hello_world/requirements.txt
COPY ./env.sh ./env.sh
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

RUN ["pip", "install","-r", "./hello_world/requirements.txt"]
#CMD ["ls"]
CMD ["/bin/bash", "-c", "source ./env.sh && python -m hello_world.app"]