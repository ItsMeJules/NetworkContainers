from redis import Redis
from pymongo import MongoClient
from threading import Lock

mutex = Lock()

AUTOSAVE_INTERVAL_SECONDS = 5 * 60

MONGODB_DATABASE_NAME = "server"
MONGODB_UUID_LOOKUP_CHANNEL_RESPONSE = "name-to-uuid"
MONGODB_UUID_LOOKUP_CHANNEL_RESPONSE_NAME_FIELD = "name"
MONGODB_UUID_LOOKUP_CHANNEL_RESPONSE_UUID_FIELD = "uuid"

REDIS_UUID_LOOKUP_CHANNEL = "name-to-uuid"
REDIS_UUID_LOOKUP_CHANNEL_RESPONSE = "response_name-to-uuid"

REDIS_PUNISHMENT_CHANNEL = "punishment"
REDIS_SERVER_HEARTBEAT_CHANNEL = "server-heartbeat"


channels = [
	REDIS_UUID_LOOKUP_CHANNEL,
	REDIS_PUNISHMENT_CHANNEL,
	REDIS_SERVER_HEARTBEAT_CHANNEL
]