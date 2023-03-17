import redis
import json

from pymongo.collection import Collection
from uuid import UUID

from constants import *

def uuid_lookup_message(message, db, redispy):
    name = message["name"]
    result = db[UUID_LOOKUP_COLLECTION].find_one({UUID_LOOKUP_COLLECTION_NAME_FIELD: name})

    data = {}
    data["name"] = result[UUID_LOOKUP_COLLECTION_NAME_FIELD] if result else name
    data["uuid"] = result[UUID_LOOKUP_COLLECTION_UUID_FIELD] if result else None

    redispy.publish(UUID_LOOKUP_CHANNEL_RESPONSE, json.dumps(data))

def punishment_message(message, db, redispy):
    print(message)

def save_data(db, redispy):
    mapped_values = {}

    for name, uuid in redispy.hgetall(UUID_LOOKUP_COLLECTION).items():
        mapped_values[name.decode('utf-8')] = UUID(uuid.decode("utf-8"))

    found_names = [doc["name"] for doc in db[UUID_LOOKUP_COLLECTION].find({'name': {'$in': list(mapped_values.keys())}})]
    found_names_len = len(found_names)

    if (found_names_len != 0):
        filter_found = {'name': {'$in': found_names}}
        documents_to_update = [{'$set': {'uuid': str(mapped_values[name]) for name in found_names}}]
        db[UUID_LOOKUP_COLLECTION].update_many(filter_found, documents_to_update)

    if (found_names_len != len(mapped_values.keys())):
        documents_to_insert = [{'name': name, 'uuid': str(mapped_values[name])} for name in set(mapped_values.keys()) - set(found_names)]
        db[UUID_LOOKUP_COLLECTION].insert_many(documents_to_insert)

def server_heartbeat_message(message, db: Collection, redispy: redis.Redis):
    status = message["status"]

    if (status == "started"):
        print("started")
    elif (status == "stopped"):
        print("stopped")
        save_data(db, redispy)

message_handling_map = {
    UUID_LOOKUP_CHANNEL: uuid_lookup_message,
    PUNISHMENT_CHANNEL: punishment_message,
    REDIS_SERVER_HEARTBEAT_CHANNEL: server_heartbeat_message
}

def pubsub_listener(pubsub, db, redispy):
    for message in pubsub.listen():
        if (message["type"] != "message"):
            continue

        channel = message["channel"].decode("utf-8")
        print("message received on channel:", channel)

        if channel in message_handling_map:
            with mutex:
                message_data = message["data"].decode("utf-8")
                message_handling_map[channel](json.loads(message_data), db, redispy)