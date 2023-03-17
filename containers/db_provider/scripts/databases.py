import pymongo

from constants import *
from channel_handler import pubsub_listener

def init_pubsub(redispy):
    pubsub = redispy.pubsub()

    print(f"subscribing to channels {channels}...")
    for channel in channels:
        pubsub.subscribe(UUID_LOOKUP_CHANNEL, PUNISHMENT_CHANNEL, REDIS_SERVER_HEARTBEAT_CHANNEL)
    
    return pubsub

def init_mongodb(mongo):
    print("initializing collections...")
    init_collections(mongo[DATABASE_NAME], UUID_LOOKUP_COLLECTION)

def init_collections(db, *names):
    collections_name = db.list_collection_names()
    print(f"{len(collections_name)} collections found.")
    print(collections_name)
    
    for name in names:
        if (name in collections_name):
            continue

        print("creating collection", name)

        if name == UUID_LOOKUP_COLLECTION:
            collection = db[UUID_LOOKUP_COLLECTION]
            collection.create_index([(UUID_LOOKUP_COLLECTION_NAME_FIELD, pymongo.ASCENDING)])