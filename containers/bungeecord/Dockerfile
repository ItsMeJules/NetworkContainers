FROM openjdk:8-jdk-alpine

EXPOSE 25577

RUN apk update && apk upgrade \
	&& apk add wget

# create a user to run the bungeecord server
# sudo useradd bungeecord -r -m -d /opt/bungeecord

WORKDIR /proxy
COPY scripts/ .
# add execute option to user only
RUN chmod +x launch_proxy.sh

WORKDIR /proxy/proxy_files
COPY configs/ .

WORKDIR /proxy

ENTRYPOINT ["sh", "launch_proxy.sh"]