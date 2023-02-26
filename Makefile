NAME 	=	network

all		:	${NAME}

${NAME}	:	build up

build: volume
	docker-compose build

volume:
	mkdir -p /home/jules/Dev/Java/Minecraft/network/network_containers/data/main_server
	
	mkdir -p /home/jules/Dev/Java/Minecraft/network/network_containers/data/hub_server

	mkdir -p /home/jules/Dev/Java/Minecraft/network/network_containers/data/bungeecord/

	mkdir -p /home/jules/Dev/Java/Minecraft/network/network_containers/data/redis/

rmvolume:
	rm -rf data/*

connect_main_server:
	docker attach main_server

container_tty:
	docker exec -it main_server sh

up:
	docker-compose up -d --remove-orphans

down:
	docker-compose down

stop:
	docker-compose stop

rm: stop
	docker-compose rm

re: clean ${NAME}

.PHONY: all clean fclean re bonus