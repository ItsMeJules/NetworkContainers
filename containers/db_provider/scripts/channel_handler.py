import redis
import json

from pymongo.collection import Collection

from constants import *
from database_saver import save_data


def uuid_lookup_message(message, db, redispy):
    name = message["name"]
    result = db[MONGODB_UUID_LOOKUP_COLLECTION].find_one({MONGODB_UUID_LOOKUP_COLLECTION_NAME_FIELD: name})

    data = {"server-id": message["server-id"],
            "name": result[MONGODB_UUID_LOOKUP_COLLECTION_NAME_FIELD] if result else name,
            "uuid": result[MONGODB_UUID_LOOKUP_COLLECTION_UUID_FIELD] if result else None}

    redispy.publish(REDIS_UUID_LOOKUP_RESPONSE_CHANNEL, json.dumps(data))


def punishment_message(message, db, redispy):
    print(message)


def server_heartbeat_message(message, db: Collection, redispy: redis.Redis):
    status = message["status"]

    if status == "started":
        print("started")
    elif status == "stopped":
        print("stopped")
        save_data(db, redispy)


message_handling_map = {
    REDIS_UUID_LOOKUP_CHANNEL: uuid_lookup_message,
    REDIS_PUNISHMENT_CHANNEL: punishment_message,
    REDIS_SERVER_HEARTBEAT_CHANNEL: server_heartbeat_message
}


def pubsub_listener(pubsub, db, redispy):
    for message in pubsub.listen():
        if message["type"] != "message":
            continue

        channel = message["channel"].decode("utf-8")
        print("message received on channel:", channel)

        if channel in message_handling_map:
            with mutex:
                message_data = message["data"].decode("utf-8")
                message_handling_map[channel](json.loads(message_data), db, redispy)
