from redis import Redis
from pymongo import MongoClient
from threading import Lock

mutex = Lock()
redispy: Redis = None
mongo: MongoClient = None

AUTOSAVE_INTERVAL_SECONDS = 1 * 5

DATABASE_NAME = "server"
UUID_LOOKUP_COLLECTION = "name-to-uuid"
UUID_LOOKUP_COLLECTION_NAME_FIELD = "name"

UUID_LOOKUP_CHANNEL = "name-to-uuid"
PUNISHMENT_CHANNEL = "punishment"