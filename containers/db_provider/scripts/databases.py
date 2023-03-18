import pymongo

from constants import *


def init_pubsub(redispy):
    pubsub = redispy.pubsub()

    print(f"subscribing to channels {channels}...")
    for channel in channels:
        pubsub.subscribe(REDIS_UUID_LOOKUP_CHANNEL, REDIS_PUNISHMENT_CHANNEL, REDIS_SERVER_HEARTBEAT_CHANNEL)

    return pubsub


def init_redis_database(redispy, db):
    doc = db[MONGODB_IDS_COLLECTION].find_one({MONGODB_IDS_COLLECTION_TYPE_FIELD: {"$eq": "punishments"}})
    redispy.set(REDIS_PUNISHMENTS_LAST_ID_KEY, doc["last-id"])


def init_mongodb(mongo):
    print("initializing collections...")
    init_collections(mongo[MONGODB_DATABASE_NAME], MONGODB_UUID_LOOKUP_COLLECTION, MONGODB_IDS_COLLECTION)


def init_collections(db, *names):
    collections_name = db.list_collection_names()
    print(f"{len(collections_name)} collections found.")
    print(collections_name)

    for name in names:
        if name in collections_name:
            continue

        print("creating collection", name)

        if name == MONGODB_UUID_LOOKUP_COLLECTION:
            collection = db[MONGODB_UUID_LOOKUP_COLLECTION]
            collection.create_index([(MONGODB_UUID_LOOKUP_COLLECTION_NAME_FIELD, pymongo.ASCENDING)])
        elif name == MONGODB_IDS_COLLECTION:
            collection = db[MONGODB_IDS_COLLECTION]
            collection.create_index([(MONGODB_IDS_COLLECTION_TYPE_FIELD, pymongo.ASCENDING)])
            collection.insert_many([{"type": "punishments", "last-id": 0},
                                    {"type": "reports", "last-id": 0}])
