FROM openjdk:8-jdk-alpine

EXPOSE 25565

RUN apk update && apk upgrade \
	&& apk add wget

# create a user to run the minecraft server
# sudo useradd minecraft -r -m -d /opt/minecraft

WORKDIR /server
COPY scripts/ .
# add execute option to user only
RUN chmod +x launch_server.sh

WORKDIR /server/server_files
COPY configs/ paper-1.8.8.jar /server/server_files/

WORKDIR /server
ENTRYPOINT ["sh", "launch_server.sh"]