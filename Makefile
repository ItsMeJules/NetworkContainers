NAME 	=	network

all		:	${NAME}

${NAME}	:	build up

build: volume
	sudo docker-compose build

volume:
	sudo mkdir -p /home/jules/Dev/Java/Minecraft/network/data/main_server
	
	sudo mkdir -p /home/jules/Dev/Java/Minecraft/network/data/hub_server

	sudo mkdir -p /home/jules/Dev/Java/Minecraft/network/data/bungeecord/

	sudo mkdir -p /home/jules/Dev/Java/Minecraft/network/data/redis/

rmvolume:
	sudo rm -rf data/*

connect_main_server:
	sudo docker attach main_server

container_tty:
	sudo docker exec -it main_server sh

up:
	sudo docker-compose up -d --remove-orphans

down:
	sudo docker-compose down

stop:
	sudo docker-compose stop

rm: stop
	sudo docker-compose rm

re: clean ${NAME}

.PHONY: all clean fclean re bonus