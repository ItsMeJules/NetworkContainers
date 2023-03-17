from redis import Redis
from pymongo import MongoClient
from threading import Lock

mutex = Lock()

AUTOSAVE_INTERVAL_SECONDS = 5 * 60

DATABASE_NAME = "server"
UUID_LOOKUP_COLLECTION = "name-to-uuid"
UUID_LOOKUP_COLLECTION_NAME_FIELD = "name"
UUID_LOOKUP_COLLECTION_UUID_FIELD = "uuid"

UUID_LOOKUP_CHANNEL = "name-to-uuid"
UUID_LOOKUP_CHANNEL_RESPONSE = "response_name-to-uuid"

PUNISHMENT_CHANNEL = "punishment"
REDIS_SERVER_HEARTBEAT_CHANNEL = "server-heartbeat"

channels = [
	UUID_LOOKUP_CHANNEL,
	PUNISHMENT_CHANNEL,
	REDIS_SERVER_HEARTBEAT_CHANNEL
]