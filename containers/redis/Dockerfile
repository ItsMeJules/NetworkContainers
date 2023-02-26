FROM redis:latest

EXPOSE 6379

COPY configs/redis.conf /usr/local/etc/redis/

ENTRYPOINT [ "redis-server", "/usr/local/etc/redis/redis.conf" ]