import redis

from constants import *

def uuid_lookup_message(message, db):
    name = message["name"].decode("utf-8")
    result = db['name-to-uuid'].find_one({'name': name})

    redis.publish(UUID_LOOKUP_CHANNEL, result['uuid'] if result else None)

def punishment_message(message, db):
    print(message)

def proxy_heartbeat_message(message, db):
    print()
    
message_handling_map = {
    UUID_LOOKUP_CHANNEL: uuid_lookup_message,
    PUNISHMENT_CHANNEL: punishment_message
}

def pubsub_listener(pubsub, db):
    for message in pubsub.listen():
        if (message["type"] != "message"):
            continue

        channel = message["channel"].decode("utf-8")
        print("message received on channel:", channel)

        if channel in message_handling_map:
            with mutex:
                message_handling_map[channel](message["data"], db)