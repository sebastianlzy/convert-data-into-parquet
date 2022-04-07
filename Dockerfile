#Deriving the latest base image
FROM python:latest


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /

#to COPY the remote file at working directory in container
COPY ./app/requirements.txt ./app/requirements.txt
COPY ./env.sh ./env.sh
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

RUN ["pip", "install","-r", "./app/requirements.txt"]
#CMD ["ls"]
#CMD ["/bin/bash", "-c", "source ./env.sh && python -m app.main"]
#CMD ["/bin/bash", "-c", "source ./env.sh && python -m app.load_to_dynamoDB"]
CMD ["/bin/bash", "-c", "source ./env.sh && python -m app.read_from_dynamoDB"]